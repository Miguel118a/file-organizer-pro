from models.file import File
from core.logger import Logger
from core.history import History
from core import estrategy
from langs.translator import Translator
import os
import shutil

class Organizer:
    """
    Organizes files in a folder by moving them to subfolders
    according to the chosen criteria (type, date, size).
    """
    
    def __init__(self, path, categories, ignore, criteria=None, cleanup="", max_history=10, translator=None):
        """
        Args:
            path: Root folder to organize.
            categories: Dictionary {category: [extensions]} from config.json.
            ignore: List of filenames that the program skips.
            criteria: Ordered list of criteria ('type', 'date', 'size').
            cleanup: 'yes' to delete empty folders upon completion.
            max_history: Maximum number of entries saved in history.
            translator: Translator object for i18n.
        """
        
        self.path = path
        self.criteria = criteria if criteria else []
        self.cleanup = cleanup
        if translator is None:
            translator = Translator(lang="en")
        self.translator = translator
        self.logger = Logger(os.path.join(self.path, "log.txt"), self.translator)
        self.ignore = ignore
        self.categories = categories
        self.max_history = max_history
        self.last_summary = {"details": {}, "total": 0}
        
    def scan(self):
        """
        Lists all direct files in self.path (does not enter subfolders).
        Returns a list of File objects.
        """
        try:
            file_objects_list = []
            filenames = os.listdir(self.path)
            for name in filenames:
                full_path = os.path.join(self.path, name)
                if os.path.isfile(full_path):
                    new_file = File(full_path)
                    file_objects_list.append(new_file)
        except FileNotFoundError:
            print(self.translator.get("Error: Path not found {path}", path=self.path))
        except PermissionError:
            print(self.translator.get("Error: You do not have permissions to access {path}", path=self.path))
        except Exception as e:
            print(self.translator.get("Unexpected error while scanning: {e}", e=e))

        return file_objects_list

    def filter(self):
        """
        Applies criteria to each file and decides its destination folder.
        If there are multiple criteria, they are nested as subfolders (e.g., 'Images/2024/January').
        Returns a dictionary {File: Relative_destination_path}.
        """
        file_list = self.scan()
        result = {}
        for f in file_list:
            if f.name in self.ignore or f.name.startswith("."):
                continue
            destination_layers = []
            for criterio in self.criteria:    
                if criterio == "date":
                    destination_layers.append(estrategy.get_by_date(f, self.translator))
                elif criterio == "type":
                    destination_layers.append(estrategy.get_by_type(f, self.categories, self.translator))
                elif criterio == "size":
                    destination_layers.append(estrategy.get_by_size(f, self.translator))
            if not destination_layers:
                final_destination = "" 
            else:
                final_destination = os.path.join(*destination_layers)
            result[f] = final_destination
        return result
    
    def simulate(self):
        """
        Shows what move() would do without actually moving anything.
        Returns (dict {folder: [names]}, total).
        """
        simulator = self.filter()
        result = {}
        total = 0
        for file_obj, folder in simulator.items():
            if folder not in result:
                result[folder] = []
            result[folder].append(file_obj.name)
            total += 1
        return result, total                   
    
    def cleanup_empty_folders(self):
        """
        Traverses self.path from bottom to top and deletes folders that were left empty.
        Executes only if self.cleanup == 'yes'.
        """
        for root, dirs, files in os.walk(self.path, topdown=False):
            for folder in dirs:
                full_path = os.path.join(root, folder)
                try:
                    if not os.listdir(full_path):
                        os.rmdir(full_path)
                        self.logger.log_cleanup(folder)
                except Exception as e:
                    self.logger.log_error(folder, f"Could not delete: {e}")
                
    def move(self):
        """
        Moves files to their destination folders according to filter().
        Saves the result in history and in the log.
        If a file already exists at that destination, adds a counter: file(1).ext.
        Returns the summary with details, total, tracking, and new_folders.
        """
        files_to_move = self.filter()
        session_summary = {}
        detailed_tracking = []
        total_moved = 0
        created_folders = []
        
        for file_obj, folder in files_to_move.items():
            try:
                folder_path = os.path.join(self.path, folder)
                if not os.path.exists(folder_path):
                    created_folders.append(folder_path)
                    
                final_path = os.path.join(self.path, folder, file_obj.name)
                final_name = file_obj.name
                
                if os.path.abspath(file_obj.full_path) == os.path.abspath(final_path):
                    continue
                
                counter = 1
                while os.path.exists(final_path):
                    new_name = f"{file_obj.name_no_ext}({counter}){file_obj.extension}"
                    final_path = os.path.join(self.path, folder, new_name)
                    final_name = new_name
                    counter += 1        
                           
                os.makedirs(folder_path, exist_ok=True)
                
                # Try to move - os.rename() fails immediately if file is locked
                try:
                    try:
                        os.rename(file_obj.full_path, final_path)
                    except OSError:
                        shutil.move(file_obj.full_path, final_path)
                except (PermissionError, OSError) as move_error:
                    # File is locked or cannot be accessed - do NOT use shutil.move() as it creates copies
                    error_msg = f"Cannot move (file locked or in use): {move_error}"
                    print(f"[!] {error_msg} - {file_obj.name}")
                    self.logger.log_error(file_obj.name, error_msg)
                    continue
                
                # Only add to tracking if move was successful
                final_path_destination = os.path.join(self.path, folder, final_name)
                detailed_tracking.append({
                    "origin": file_obj.full_path,
                    "destination": final_path_destination
                })
                
                session_summary[folder] = session_summary.get(folder, 0) + 1
                total_moved += 1
                self.logger.log_movement(final_name, folder)
                
            except Exception as e:
                self.logger.log_error(file_obj.name, e)
                
        if self.cleanup == "yes":
            print(self.translator.get("[i] Cleaning empty directories..."))
            self.cleanup_empty_folders()
            
        self.last_summary = {
            "details": session_summary,
            "tracking": detailed_tracking,
            "new_folders": created_folders,
            "total": total_moved,
        }
        
        hist = History(max_items=self.max_history)
        hist.save_execution(self.path, self.last_summary)
        return self.last_summary
    
    def undo_movement(self, tracking_record):
        """
        Reverts the movements of a session using the tracking saved in history.
        Each tracking entry has 'origin' (where it was) and 'destination' (where it stayed).
        Returns (successes, errors).
        """
        successes = 0
        errors = 0
        print(self.translator.get("\n[!] Starting reversion process..."))
        for step in tracking_record:
            where_it_should_return = step["origin"]
            where_it_is_now = step["destination"]
            try:
                if os.path.exists(where_it_is_now):
                    os.makedirs(os.path.dirname(where_it_should_return), exist_ok=True)
                    try:
                        shutil.move(step["destination"], step["origin"])
                        successes += 1
                    except (PermissionError, OSError) as move_error:
                        # File is locked - log and continue with next file
                        error_msg = f"Cannot undo: {move_error}"
                        print(self.translator.get("[!] Permission error (file open) in {name}: {e}", name=os.path.basename(where_it_is_now), e=move_error))
                        self.logger.log_error(os.path.basename(where_it_is_now), error_msg)
                        errors += 1
                else:
                    print(self.translator.get("[-] Not found: {name}", name=os.path.basename(where_it_is_now)))
                    self.logger.log_error(os.path.basename(where_it_is_now), "File not found during undo")
                    errors += 1
            except Exception as e:
                print(self.translator.get("[!] Error returning {name}: {e}", name=os.path.basename(where_it_is_now), e=e))
                self.logger.log_error(os.path.basename(where_it_is_now), str(e))
                errors += 1
        return successes, errors
    
class Recursive_Organizer(Organizer):
    """
    Extends Organizer to include files within subfolders.
    Only overrides scan() - everything else (filter, move, etc.) is inherited.
    """
    
    def scan(self):
        """
        Traverses self.path and all its subfolders with os.walk.
        Returns a list of File objects from all levels.
        """
        file_objects_list = []
        try:
            for current_path, folders, files in os.walk(self.path):
                for file in files:
                    full_path = os.path.join(current_path, file)
                    file_objects_list.append(File(full_path))
        except Exception as e:
            print(self.translator.get("Error during recursive scan: {e}", e=e))
        return file_objects_list



def perform_undo(last, hist, translator=None):
    '''
    Executes the reversion of the last organization.
    Returns (successes, errors) and updates history + log.
    Used both from app.py (CLI) and from menu.py (interactive menu).
    
    Args:
        last: Last history record (dict with tracking, folder, etc).
        hist: History object already instantiated - used for delete_last().
        translator: Translator object for i18n (respects user's language choice).
    '''
    try:
        if translator is None:
            translator = Translator(lang="en")
        root_path = last.get("root_path", os.path.dirname(last["tracking"][0]["origin"]))
        log_path = os.path.join(root_path, "log.txt")
        temp_org = Organizer(path="", categories={}, criteria=[], ignore=[], translator=translator)
        successes, errors = temp_org.undo_movement(last["tracking"])
        if successes > 0:
            hist.delete_last()
            Logger(log_path, translator).log_undo(last["folder"], successes)
        return successes, errors
    
    except Exception as e:
        print(f"[!] Error in perform_undo: {e}")
        return 0, 0   
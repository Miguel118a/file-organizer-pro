from cli.menu import run_menu
from core.organizer import Organizer, Recursive_Organizer, perform_undo
from core.configurator import Configurator
from core.history import History
from langs.translator import Translator
import argparse
import sys, shutil, os

def get_writable_config_path():
    """
    Returns a writable path for the configuration file.
    on windows, it will be in the same folder as the executable.
    on linus and max, it will be in the same folder as the script.
    """
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "config.json")

if getattr(sys, 'frozen', False):
    config_destino = get_writable_config_path()
    if not os.path.exists(config_destino):
        config_origen = os.path.join(sys._MEIPASS, "config.json")
        shutil.copy(config_origen, config_destino)


def run_cli(args):
    """
    Executes the program in command line mode (without graphical menu).
    It is activated when the user passes arguments such as -r, --undo, etc.
    
    Args:
        args: Argparse object with the parsed arguments.    
    """
    translator = Translator(lang="en")  # default english
    config = Configurator(translator)
    language = config.get_setting("language", "en")
    if language != translator.lang:
        translator = Translator(lang=language)
        config = Configurator(translator)
        
    try:
        hist = History()
        if args.undo:
            last = hist.get_last()
            if last and last.get("tracking"):
                print(translator.get("[!] Reverting last organization in: {folder}", folder=last['folder']))
                successes, errors = perform_undo(last, hist, translator)
                if successes > 0:
                    print(translator.get("[v] Files returned: {amount}", amount=successes))
                    print(translator.get("[v] History and log updated."))
                    
                    if last.get("new_folders"):
                        print(translator.get("[i] Cleaning folders that were created..."))
                        for folder in reversed(last["new_folders"]):
                            try:
                                if os.path.exists(folder) and not os.listdir(folder):
                                    os.rmdir(folder)
                            except:
                                pass
                else:
                    print(translator.get("[!] Could not recover any file from '{folder}'.", folder=last['folder']))
                    hist.delete_last()
                    print(translator.get("[i] Invalid record removed from history."))
            else:
                print(f"\n{translator.get('[!] No tracking data to undo or history is empty.')}")
            return
    except Exception as e:
        print(f"{translator.get('An error occurred')}: {e}")
        return
        
    if not args.path:
        print(f"\n{translator.get('[!] ERROR: You must specify a path with \'-r\' to organize.')}")
        return
    
    try:
        categories = config.get_categories()
        ignore = config.get_setting("ignore", [])
        max_history = config.get_setting("max_history", 10)
        criteria = args.criteria if args.criteria else config.get_setting("default_criteria", ["type"])
        params = {
            "path": args.path, 
            "categories": categories, 
            "ignore": ignore, 
            "criteria": criteria, 
            "cleanup" : args.clean, 
            "max_history": max_history,
            "translator": translator
        }
        
        org = Recursive_Organizer(**params) if args.recursive else Organizer(**params)
        
        if args.simulate:
            print(f"\n{translator.get('[i] Starting SIMULATION in: {path}', path=args.path)}")
            summary, total = org.simulate()
            for folder, files in summary.items():
                print(f" -> {folder}: {len(files)} {translator.get('file(s)')}")
            print(f"{translator.get('Total to move')}: {total}")
        else:
            print(f"\n{translator.get('[!] Starting ORGANIZATION in: {path}', path=args.path)}")
            summary = org.move()
            for folder, amount in summary["details"].items():
                print(f" -> {folder}: {amount} {translator.get('file(s)')}")
            print(f"{translator.get('Process completed!')} {translator.get('TOTAL MOVED')}: {summary['total']}")
    except PermissionError:
        print(f"\n{translator.get('[!] ERROR: You do not have administrator permissions to move files in this path.')}")
    except FileNotFoundError:
        print(f"\n{translator.get('[!] ERROR: The specified path does not exist.')}")
    except Exception as e:
        print(f"\n{translator.get('[!] An unexpected error occurred: {e}', e=e)}")
        
def main():
    """
    Program entry point.
    If the user passes arguments (-r, --undo, etc.) --> CLI mode.
    If no arguments are passed --> opens the interactive menu.
    """
    parser = argparse.ArgumentParser(description="File Organizer Pro v3.0")
    parser.add_argument("-r", "--path", help="Path of the folder to organize")
    parser.add_argument("-rec", "--recursive", action="store_true", help="Enable recursive mode (includes subfolders)")
    parser.add_argument("-s", "--simulate", action="store_true", help="Run simulation only (without moving anything)")
    parser.add_argument("-c", "--criteria", nargs="+", help="Order criteria (e.g.: type date)")
    parser.add_argument("-l", "--clean", choices=["yes", "no"], default="no", help="Delete empty folders when finished")
    parser.add_argument("-u", "--undo", action="store_true", help="Undoes the last organization performed")

    args = parser.parse_args()
    
    config = Configurator(Translator(lang="en"))
    saved_lang = config.get_setting("language", "en")
    main_translator = Translator(lang=saved_lang)
    
    if args.path or args.undo:
        run_cli(args)
    else:
        run_menu(main_translator)
    
if __name__ == "__main__":
    main()
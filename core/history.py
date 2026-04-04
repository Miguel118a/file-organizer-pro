import os
import json
from datetime import datetime

class History:
    """Manages the history of moved files to allow undo operations."""
    
    def __init__(self, file_name="history.json", max_items=10):
        """
        Args:
            file_name: Name of the JSON file where history is stored.
            max_items: Maximum records kept (oldest are discarded).
        """
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.path = os.path.join(root_path,file_name)
        self.max_items = max_items

    def save_execution(self, root_path, summary):
        """
        Saves a new organization record in the history.
        If max_items is exceeded, deletes the oldest ones.
        
        Args:
            root_path: Path of the folder that was organized.
            summary: Dictionary with details, total, tracking, and new_folders.
        """
        folder_name = os.path.basename(root_path)
        new_entry = {
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "folder": folder_name,
            "root_path": root_path,
            "details": summary.get("details", {}),
            "total": summary.get("total", 0),
            "tracking": summary.get("tracking", []),
            "new_folders": summary.get("new_folders", [])
        }
        history_data = []
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="UTF-8") as f:
                try:
                    history_data = json.load(f)
                except json.JSONDecodeError:
                    history_data = []
        history_data.append(new_entry)
        
        if len(history_data) > self.max_items:
            history_data = history_data[-self.max_items:]
        with open(self.path, "w", encoding="UTF-8") as f:
            json.dump(history_data, f, indent=4, ensure_ascii=False)

    def get_last(self):
        """
        Returns the last record in the history, or None if empty or not found.
        """
        if not os.path.exists(self.path):
            return None
        with open(self.path, "r", encoding="UTF-8") as f:
            try: 
                data = json.load(f)
                if not data:
                    return None
                return data[-1]
            except json.decoder.JSONDecodeError:
                return None
    
    def delete_last(self):
        """
        Deletes the last record in the history.
        Called after a successful undo.
        Returns True if deleted, False if empty or error.
        """
        if not os.path.exists(self.path):
            return False
        try:
            with open(self.path, "r", encoding="UTF-8") as f:
                data = json.load(f)
            if data:
                data.pop()
                with open(self.path, "w", encoding="UTF-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                return True
        except (json.JSONDecodeError, Exception):
            return False
        return False
        
            
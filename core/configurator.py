import json
import os
import sys

class Configurator:
    """
    Reads and exposes the program configuration from config.json.
    If the file does not exist or is corrupt, uses safe default values.
    """
    
    def __init__(self, translator):
        """
        Locates config.json in the project root and loads it.
        
        Args:
            translator: Translator object for i18n.
        """
        if getattr(sys, 'frozen', False):
            root_path = os.path.dirname(sys.executable)
        else:
            root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(root_path, "config.json")
        self.translator = translator
        self.data = self._load()

    def _load(self):
        """
        Loads config.json and normalizes extensions to lowercase.
        If it fails, returns a dictionary with safe default values.
        """
        default_config = {
                "settings": {
                    "language": "en",
                    "max_history": 10,
                    "ignore": [".DS_Store", "desktop.ini"]
                },
                "categories": {
                "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".bmp", ".svg", ".ico", ".tiff", ".raw", ".heic"],
                "Media": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus"],
                "Documents": [".psc", ".txt", ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".odt", ".ods", ".odp", ".rtf", ".epub"],
                "Codes": [".py", ".js", ".html", ".css", ".ts", ".json", ".xml", ".php", ".java", ".cpp", ".c", ".cs", ".rb", ".go", ".rs", ".kt", ".swift"],
                "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
                "Apps": [".exe", ".msi", ".msix", ".apk", ".dmg", ".deb", ".rpm", ".bat", ".sh", ".jar", ".appimage"]
            }
            }
        
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r", encoding="UTF-8") as f:
                    data = json.load(f)
                    
                    if "settings" not in data:
                        data["settings"] = default_config["settings"]
                    if "categories" not in data:
                        data["categories"] = default_config["categories"]
                        
                    if "categories" in data:
                        for cat, exts in data["categories"].items():
                            data["categories"][cat] = [e.lower().strip() for e in exts]
                    return data
            else:
                return default_config
                 
        except Exception as e:
            error_msg = self.translator.get("config_error", e=e)
            print(error_msg)
            return default_config
    
    def set_setting(self, key, value):
        """
        Updates a setting in the config data and saves it to config.json.
        
        Args:
            key: Setting name (e.g., 'language').
            value: New value for the setting.
        """
        if "settings" not in self.data:
            self.data["settings"] = {}
        self.data["settings"][key] = value
        try:
            with open(self.file_path, "w", encoding="UTF-8") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            error_msg = self.translator.get("config_error", e=e)
            print(error_msg)
        
    def get_setting(self, key, default_value=None):
        """
        Returns a setting from the 'settings' section of the config.
        If the key does not exist, returns default_value.
        
        Args:
            key: Setting name (e.g., 'max_history', 'ignore').
            default_value: Value to return if the key does not exist.
        """
        return self.data.get("settings", {}).get(key, default_value)

    def get_categories(self):
        """Returns the categories dictionary with its extensions."""
        return self.data.get("categories", {})
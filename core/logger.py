from datetime import datetime

class Logger:
    """Handles the activity log for file movements."""
    
    def __init__(self, path, translator):
        """
        Args:
            path: Path to the log.txt file.
            translator: Translator object for i18n.
        """
        self.path = path
        self.translator = translator
        
    def _write(self, message):
        """Writes a line with date and time in the log."""
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        line = f"[{current_date}] {message}\n"
        with open(self.path, "a", encoding="UTF-8") as f:
            f.write(line)

    def log_movement(self, file_name, destination):
        """Records that a file was moved to a destination folder."""
        text = self.translator.get("log_movement", file_name=file_name, destination=destination)
        self._write(text)
                        
    def log_error(self, file_name, error):
        """Records that a file could not be moved."""
        text = self.translator.get("log_error", file_name=file_name, error=error)
        self._write(text)
        
    def log_cleanup(self, folder_name):
        """Records that an empty folder was deleted."""
        text = self.translator.get("log_cleanup", folder_name=folder_name)
        self._write(text)
    
    def log_undo(self, folder, amount):
        """Records that a successful undo was performed."""
        text = self.translator.get("log_undo", folder=folder, amount=amount)
        self._write(text)
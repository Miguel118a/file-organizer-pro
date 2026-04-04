import os

class File:
    """Represents a system file with its basic attributes."""
    
    def __init__(self, full_path):
        """
        Args:
            full_path: Absolute path to the file in the system.
        """
        self.full_path = full_path
        self.name = os.path.basename(full_path)
        self.extension = os.path.splitext(self.name)[1]
        self.name_no_ext = os.path.splitext(self.name)[0]
        self.parent_path = os.path.dirname(self.full_path)
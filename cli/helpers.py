import tkinter as tk
from tkinter import filedialog, messagebox
import os
import platform
import re
from langs.translator import Translator

def is_protected_folder(path: str, translator: Translator) -> tuple[bool, str]:
    """
    Checks if a path is an operating system folder that should not be touched.
    Protects against grave errors like organizing C:\\Windows or /etc.
    
    Returns (True, motive) if it is dangerous, (False, "") if it is safe.
    
    Args:
        path: Absolute path to verify.
        translator: Translator object for i18n.
    """
    path = os.path.normpath(os.path.abspath(path))
    system = platform.system()
    protected_paths = set()
    
    if system == "Windows":
        
        import string
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                protected_paths.add(drive.lower())
    
        windir = os.environ.get("WINDIR", "C:\\Windows")
        programfiles = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        programfiles_x86 = os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)")
        systemroot = os.environ.get("SYSTEMROOT", "C:\\Windows")
        
        protected_paths.update([
            windir.lower(),
            programfiles.lower(),
            programfiles_x86.lower(),
            systemroot.lower(),
            os.path.join(systemroot, "System32").lower(),
            os.path.join(systemroot, "SysWOW64").lower(),
            os.path.join(systemroot, "WinSxS").lower(),
            "c:\\users", "c:\\programdata", "c:\\recovery", 
            "c:\\$recycle.bin", "c:\\system volume information",
        ])
        
    elif system == "Darwin":
        protected_paths.update([ 
            "/", "/bin", "/sbin", "/usr", "/usr/bin", "/usr/sbin", 
            "/usr/local", "/usr/lib", "/system", "/library", "/private", 
            "/private/var", "/private/etc", "/volumes", "/applications", 
            "/cores", "/dev", "/etc", "/var", "/network", "/home",
    ])
        
    else: # Linux
        protected_paths.update([
            "/", "/bin", "/sbin", "/usr", "/usr/bin", "/usr/sbin", 
            "/usr/local", "/usr/lib", "/usr/share", "/lib", "/lib64", 
            "/etc", "/boot", "/dev", "/proc", "/sys", "/run", "/tmp", 
            "/var", "/var/log", "/var/lib", "/root", "/snap", "/opt", 
            "/srv", "/media", "/mnt",
        ])
        
    path_check = path.lower() if system == "Windows" else path
    if path_check in protected_paths:
        motive = translator.get("Protected system path: '{path}'", path=path)
        return True, motive
    
    folder_name = os.path.basename(path).lower()
    dangerous_patterns = [
        r"^windows$", r"^system32$", r"^syswow64$", r"^winsxs$",
        r"^program files.*", r"^programdata$", r"^\$recycle\.bin$",
        r"^system volume information$", r"^recovery$",
        r"^\.trashes$", r"^\.spotlight-v100$", r"^\.fseventsd$",
        r"^proc$", r"^sys$", r"^dev$", r"^boot$",
        r"^\.git$",
    ]
    for pattern in dangerous_patterns:
        if re.match(pattern, folder_name):
            motive = translator.get("System folder detected by name: '{name}'", name=os.path.basename(path))
            return True, motive
    return False, ""


def select_path(translator: Translator):
    """
    Opens a graphical dialog (tkinter) for the user to choose a folder.
    Verifies it's not a protected system folder before returning it.
    Returns the selected path, or None if the user canceled or chose an invalid path.
    """
    root = tk.Tk()
    root.withdraw()
    
    title = translator.get("Select a folder")
    path = filedialog.askdirectory(title=title)
    
    if not path:
        print(translator.get("No folder was selected."))
        root.destroy()
        return None
    
    protected, motive = is_protected_folder(path, translator)
    if protected:
        error_title = translator.get("Folder not allowed")
        error_msg = translator.get(
            "You cannot use this folder as a destination.\n\nMotive: {motive}\n\nPlease select a folder inside your Documents or Desktop.",
            motive=motive
        )
        messagebox.showerror(error_title, error_msg)
        root.destroy()
        return None
    
    root.destroy()
    return path
    
def ask_option(message, limit, translator: Translator):
    """
    Asks the user for a number between 1 and limit, retrying until valid.
    
    Args: 
        message: Text shown when asking for input.
        limit: Maximum accepted number (inclusive).
        translator: Translator object for i18n.
    """
    while True:
        num = input(message).strip()
        if num.isdigit() and 0 < int(num) <= limit:
            return int(num)
        print(translator.get("Please enter a number from 1 to {limit}", limit=limit))

def confirm_yes_no(message, translator: Translator):
    """
    Asks the user to answer 'yes' or 'no', retrying until valid.
    
    Args: 
        message: Text shown when asking for input.
        translator: Translator object for i18n.
    """
    valid_yes = translator.get("valid_yes") 
    valid_no = translator.get("valid_no") 
    accepted_yes = {valid_yes.lower(), "yes"}
    accepted_no = {valid_no.lower(), "no"}
    while True:
        r = input(message).strip().lower()
        if r in accepted_yes:
            return "yes"
        if r in accepted_no:
            return "no"
        print(translator.get("Only 'yes' or 'no' responses are allowed"))

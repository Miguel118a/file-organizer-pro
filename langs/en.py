LANGUAGE_NAME = "English"

MESSAGES = {
    # Months
    1: "January", 2: "February", 3: "March", 
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December",
    
    # Sizes
    "light": "Light",
    "medium": "Medium",
    "heavy": "Heavy",
    
    # Logger
    "log_movement": "MOVEMENT: {file_name} --> {destination}",
    "log_error": "ERROR: Failed to move {file_name}. Reason: {error}",
    "log_cleanup": "CLEANUP: Empty folder deleted --> {folder_name}",
    "log_undo": "UNDO: Complete reversion in {folder}. Files returned: {amount}",
    
    # Configurator
    "config_error": "[!] Critical error in config.json: {e}",
    "Images": "Images",
    "Media": "Media",
    "Documents": "Documents",
    "Codes": "Codes",
    "Compressed": "Compressed",
    "Apps": "Apps",
    "Others": "Others",
    
    # --- Organizer: Scanning errors ---
    "Error: Path not found {path}": "Error: Path not found {path}",
    "Error: You do not have permissions to access {path}": "Error: You do not have permissions to access {path}",
    "Unexpected error while scanning: {e}": "Unexpected error while scanning: {e}",
    "Error during recursive scan: {e}": "Error during recursive scan: {e}",
    # --- Organizer: Operation messages ---
    "[i] Cleaning empty directories...": "[i] Cleaning empty directories...",
    
    # --- Organizer: Undo process ---
    "\n[!] Starting reversion process...": "\n[!] Starting reversion process...",
    "[-] Not found: {name}": "[-] Not found: {name}",
    "[!] Permission error (file open) in {name}: {e}": "[!] Permission error (file open) in {name}: {e}",
    " [i] Cleanup: Partial copy in root was deleted.": " [i] Cleanup: Partial copy in root was deleted.",
    "[!] Error returning {name}: {e}": "[!] Error returning {name}: {e}",
    
    # Helpers / UI
    "Protected system path: '{path}'": "Protected system path: '{path}'",
    "System folder detected by name: '{name}'": "System folder detected by name: '{name}'",
    "Select a folder": "Select a folder",
    "No folder was selected.": "No folder was selected.",
    "Folder not allowed": "Folder not allowed",
    "You cannot use this folder as a destination.\n\nMotive: {motive}\n\nPlease select a folder inside your Documents or Desktop.": "You cannot use this folder as a destination.\n\nMotive: {motive}\n\nPlease select a folder inside your Documents or Desktop.",
    "Please enter a number from 1 to {limit}": "Please enter a number from 1 to {limit}",
    "Only 'yes' or 'no' responses are allowed": "Only 'yes' or 'no' responses are allowed",
    
    # --- Menu titles and options ---
    "FILE ORGANIZER PRO v3.0": "FILE ORGANIZER PRO v3.0",
    "Organize folder": "Organize folder",
    "Simulate organization": "Simulate organization",
    "View last summary": "View last summary",
    "Undo last organization": "Undo last organization",
    "Change language": "Change language",
    "Exit": "Exit",
    "Select an option (1-6): ": "Select an option (1-6): ",
    "AVAILABLE CATEGORIES": "AVAILABLE CATEGORIES",
    "Select categories by number separated by comma (e.g.: 1, 2, 3): ": "Select categories by number separated by comma (e.g.: 1, 2, 3): ",
    "is not a valid number. Try again.": "is not a valid number. Try again.",
    "Number {num} is out of range. Try again.": "Number {num} is out of range. Try again.",
    "ORGANIZATION CRITERIA": "ORGANIZATION CRITERIA",
    "By Date (Year/Month)": "By Date (Year/Month)",
    "By Type (Image, Document...)": "By Type (Image, Document...)",
    "By Size (Light, Medium, Heavy)": "By Size (Light, Medium, Heavy)",
    "\nSelect the order of criteria separated by comma (e.g.: 2,1): ": "\nSelect the order of criteria separated by comma (e.g.: 2,1): ",
    "is not a valid option.": "is not a valid option.",
    "Choose category mode:": "Choose category mode:",
    "All categories": "All categories",
    "Customize categories": "Customize categories",
    "\nSelect an option (1-2): ": "\nSelect an option (1-2): ",

    # --- Status and processes ---
    "Error: The selected path is no longer available.": "Error: The selected path is no longer available.",
    "Press Enter to continue...": "Press Enter to continue...",
    "\nDo you want to include subfolders? (yes/no): ": "\nDo you want to include subfolders? (yes/no): ",
    "\nDo you want to delete folders that remain empty after organization? (yes/no): ": "\nDo you want to delete folders that remain empty after organization? (yes/no): ",
    "Analyzing files and folders...": "Analyzing files and folders...",
    "Organizing, please do not close the program...": "Organizing, please do not close the program...",
    "Generating preview...": "Generating preview...",
    "PREVIEW (SIMULATION)": "PREVIEW (SIMULATION)",
    "Total that would be moved": "Total that would be moved",
    "RESULT": "RESULT",
    "file(s)": "file(s)",
    "Total": "Total",
    "A critical error occurred during the process:": "A critical error occurred during the process:",
    "Detail": "Detail",
    "Press Enter to return to the menu...": "Press Enter to return to the menu...",

    # --- History and Undo ---
    "LAST EXECUTION": "LAST EXECUTION",
    "Folder": "Folder",
    "TOTAL MOVED": "TOTAL MOVED",
    "No execution history available.": "No execution history available.",
    "Perform an organization to generate the first record.": "Perform an organization to generate the first record.",
    "RECOVERY SECTION": "RECOVERY SECTION",
    "Last folder organized": "Last folder organized",
    "Files to return": "Files to return",
    "\nAre you sure you want to revert these changes? (yes/no): ": "\nAre you sure you want to revert these changes? (yes/no): ",
    "Process completed!": "Process completed!",
    "Recovered": "Recovered",
    "Failed/Not found": "Failed/Not found",
    "\nDo you want to delete the folders created by the organizer? (yes/no): ": "\nDo you want to delete the folders created by the organizer? (yes/no): ",
    "Folder deleted": "Folder deleted",
    "Nothing found to return. Files are no longer there.": "Nothing found to return. Files are no longer there.",
    "Do you want to delete this invalid record from history? (yes/no): ": "Do you want to delete this invalid record from history? (yes/no): ",
    "Operation canceled.": "Operation canceled.",
    "No tracking data to undo or history is empty.": "No tracking data to undo or history is empty.",
    "An error occurred": "An error occurred",
    "Are you sure you want to exit the program? (yes/no): ": "Are you sure you want to exit the program? (yes/no): ",
    # --- app.py: Undo / Reversion ---
    "[!] Reverting last organization in: {folder}": "[!] Reverting last organization in: {folder}",
    "[v] Files returned: {amount}": "[v] Files returned: {amount}",
    "[v] History and log updated.": "[v] History and log updated.",
    "[i] Cleaning folders that were created...": "[i] Cleaning folders that were created...",
    "[!] Could not recover any file from '{folder}'.": "[!] Could not recover any file from '{folder}'.",
    "[i] Invalid record removed from history.": "[i] Invalid record removed from history.",
    "[!] No tracking data to undo or history is empty.": "[!] No tracking data to undo or history is empty.",

    # --- app.py: CLI Errors & Validation ---
    "[!] ERROR: You must specify a path with '-r' to organize.": "[!] ERROR: You must specify a path with '-r' to organize.",
    "[!] ERROR: You do not have administrator permissions to move files in this path.": "[!] ERROR: You do not have administrator permissions to move files in this path.",
    "[!] ERROR: The specified path does not exist.": "[!] ERROR: The specified path does not exist.",
    "[!] An unexpected error occurred: {e}": "[!] An unexpected error occurred: {e}",

    # --- app.py: Organization & Simulation ---
    "[i] Starting SIMULATION in: {path}": "[i] Starting SIMULATION in: {path}",
    "[!] Starting ORGANIZATION in: {path}": "[!] Starting ORGANIZATION in: {path}",
    "Total to move": "Total to move",
    
    # --- CHANGE LANGUAGE ---
    "CHANGE LANGUAGE": "CHANGE LANGUAGE",
    "Select language (1-2): ": "Select language (1-2): ",
    "Select an option (1-{max_option}): ": "Select an option (1-{max_option}): ",
    "valid_yes": "yes",
    "valid_no": "no",
}

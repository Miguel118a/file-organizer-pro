LANGUAGE_NAME = "Italiano"

MESSAGES = {
    # Months
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 
    4: "Aprile", 5: "Maggio", 6: "Giugno",
    7: "Luglio", 8: "Agosto", 9: "Settembre",
    10: "Ottobre", 11: "Novembre", 12: "Dicembre",
    
    # Sizes
    "light": "Leggero",
    "medium": "Medio",
    "heavy": "Pesante",
    
    # Logger
    "log_movement": "SPOSTAMENTO: {file_name} --> {destination}",
    "log_error": "ERRORE: Impossibile spostare {file_name}. Motivo: {error}",
    "log_cleanup": "PULIZIA: Cartella vuota eliminata --> {folder_name}",
    "log_undo": "ANNULLA: Ripristino completo in {folder}. File restituiti: {amount}",
    
    # Configurator
    "config_error": "[!] Errore critico in config.json: {e}",
    "Images": "Immagini",
    "Media": "Media",
    "Documents": "Documenti",
    "Codes": "Codice",
    "Compressed": "Compressi",
    "Apps": "Applicazioni",
    "Others": "Altro",
    
    # --- Organizer: Scanning errors ---
    "Error: Path not found {path}": "Errore: Percorso non trovato {path}",
    "Error: You do not have permissions to access {path}": "Errore: Non hai i permessi per accedere a {path}",
    "Unexpected error while scanning: {e}": "Errore imprevisto durante la scansione: {e}",
    "Error during recursive scan: {e}": "Errore durante la scansione ricorsiva: {e}",
    
    # --- Organizer: Operation messages ---
    "[i] Cleaning empty directories...": "[i] Pulizia delle cartelle vuote...",
    
    # --- Organizer: Undo process ---
    "\n[!] Starting reversion process...": "\n[!] Avvio processo di ripristino...",
    "[-] Not found: {name}": "[-] Non trovato: {name}",
    "[!] Permission error (file open) in {name}: {e}": "[!] Errore di permesso (file aperto) in {name}: {e}",
    " [i] Cleanup: Partial copy in root was deleted.": " [i] Pulizia: Copia parziale nella root eliminata.",
    "[!] Error returning {name}: {e}": "[!] Errore nel ripristino di {name}: {e}",
    
    # Helpers / UI
    "Protected system path: '{path}'": "Percorso di sistema protetto: '{path}'",
    "System folder detected by name: '{name}'": "Cartella di sistema rilevata dal nome: '{name}'",
    "Select a folder": "Seleziona una cartella",
    "No folder was selected.": "Nessuna cartella selezionata.",
    "Folder not allowed": "Cartella non consentita",
    "You cannot use this folder as a destination.\n\nMotive: {motive}\n\nPlease select a folder inside your Documents or Desktop.": "Non puoi usare questa cartella come destinazione.\n\nMotivo: {motive}\n\nSeleziona una cartella in Documenti o Desktop.",
    "Please enter a number from 1 to {limit}": "Inserisci un numero da 1 a {limit}",
    "Only 'yes' or 'no' responses are allowed": "Sono consentite solo risposte 'yes' o 'no'",
    
    # --- Menu titles and options ---
    "FILE ORGANIZER PRO v3.0": "FILE ORGANIZER PRO v3.0",
    "Organize folder": "Organizza cartella",
    "Simulate organization": "Simula organizzazione",
    "View last summary": "Visualizza ultimo riepilogo",
    "Undo last organization": "Annulla ultima organizzazione",
    "Change language": "Cambia lingua",
    "Exit": "Esci",
    "Select an option (1-6): ": "Seleziona un'opzione (1-6): ",
    "AVAILABLE CATEGORIES": "CATEGORIE DISPONIBILI",
    "Select categories by number separated by comma (e.g.: 1, 2, 3): ": "Seleziona le categorie per numero separate da virgola (es.: 1, 2, 3): ",
    "is not a valid number. Try again.": "non è un numero valido. Riprova.",
    "Number {num} is out of range. Try again.": "Il numero {num} è fuori intervallo. Riprova.",
    "ORGANIZATION CRITERIA": "CRITERI DI ORGANIZZAZIONE",
    "By Date (Year/Month)": "Per data (Anno/Mese)",
    "By Type (Image, Document...)": "Per tipo (Immagine, Documento...)",
    "By Size (Light, Medium, Heavy)": "Per dimensione (Leggero, Medio, Pesante)",
    "\nSelect the order of criteria separated by comma (e.g.: 2,1): ": "\nSeleziona l'ordine dei criteri separati da virgola (es.: 2,1): ",
    "is not a valid option.": "non è un'opzione valida.",
    "Choose category mode:": "Scegli modalità categoria:",
    "All categories": "Tutte le categorie",
    "Customize categories": "Personalizza categorie",
    "\nSelect an option (1-2): ": "\nSeleziona un'opzione (1-2): ",

    # --- Status and processes ---
    "Error: The selected path is no longer available.": "Errore: Il percorso selezionato non è più disponibile.",
    "Press Enter to continue...": "Premi Invio per continuare...",
    "\nDo you want to include subfolders? (yes/no): ": "\nVuoi includere le sottocartelle? (yes/no): ",
    "\nDo you want to delete folders that remain empty after organization? (yes/no): ": "\nVuoi eliminare le cartelle che rimangono vuote dopo l'organizzazione? (yes/no): ",
    "Analyzing files and folders...": "Analisi di file e cartelle...",
    "Organizing, please do not close the program...": "Organizzazione in corso, non chiudere il programma...",
    "Generating preview...": "Generazione anteprima...",
    "PREVIEW (SIMULATION)": "ANTEPRIMA (SIMULAZIONE)",
    "Total that would be moved": "Totale che verrebbe spostato",
    "RESULT": "RISULTATO",
    "file(s)": "file",
    "Total": "Totale",
    "A critical error occurred during the process:": "Si è verificato un errore critico durante il processo:",
    "Detail": "Dettaglio",
    "Press Enter to return to the menu...": "Premi Invio per tornare al menu...",

    # --- History and Undo ---
    "LAST EXECUTION": "ULTIMA ESECUZIONE",
    "Folder": "Cartella",
    "TOTAL MOVED": "TOTALE SPOSTATO",
    "No execution history available.": "Nessuna cronologia disponibile.",
    "Perform an organization to generate the first record.": "Esegui un'organizzazione per generare il primo record.",
    "RECOVERY SECTION": "SEZIONE RECUPERO",
    "Last folder organized": "Ultima cartella organizzata",
    "Files to return": "File da ripristinare",
    "\nAre you sure you want to revert these changes? (yes/no): ": "\nSei sicuro di voler annullare queste modifiche? (yes/no): ",
    "Process completed!": "Processo completato!",
    "Recovered": "Recuperati",
    "Failed/Not found": "Falliti/Non trovati",
    "\nDo you want to delete the folders created by the organizer? (yes/no): ": "\nVuoi eliminare le cartelle create dall'organizzatore? (yes/no): ",
    "Folder deleted": "Cartella eliminata",
    "Nothing found to return. Files are no longer there.": "Nessun file da ripristinare. Non esistono più.",
    "Do you want to delete this invalid record from history? (yes/no): ": "Vuoi eliminare questo record non valido dalla cronologia? (yes/no): ",
    "Operation canceled.": "Operazione annullata.",
    "No tracking data to undo or history is empty.": "Nessun dato da annullare o cronologia vuota.",
    "An error occurred": "Si è verificato un errore",
    "Are you sure you want to exit the program? (yes/no): ": "Sei sicuro di voler uscire dal programma? (yes/no): ",

    # --- app.py: Undo / Reversion ---
    "[!] Reverting last organization in: {folder}": "[!] Ripristino ultima organizzazione in: {folder}",
    "[v] Files returned: {amount}": "[v] File restituiti: {amount}",
    "[v] History and log updated.": "[v] Cronologia e log aggiornati.",
    "[i] Cleaning folders that were created...": "[i] Pulizia delle cartelle create...",
    "[!] Could not recover any file from '{folder}'.": "[!] Impossibile recuperare file da '{folder}'.",
    "[i] Invalid record removed from history.": "[i] Record non valido rimosso dalla cronologia.",
    "[!] No tracking data to undo or history is empty.": "[!] Nessun dato da annullare o cronologia vuota.",

    # --- app.py: CLI Errors & Validation ---
    "[!] ERROR: You must specify a path with '-r' to organize.": "[!] ERRORE: Devi specificare un percorso con '-r' per organizzare.",
    "[!] ERROR: You do not have administrator permissions to move files in this path.": "[!] ERRORE: Non hai i permessi amministrativi per spostare file in questo percorso.",
    "[!] ERROR: The specified path does not exist.": "[!] ERRORE: Il percorso specificato non esiste.",
    "[!] An unexpected error occurred: {e}": "[!] Si è verificato un errore imprevisto: {e}",

    # --- app.py: Organization & Simulation ---
    "[i] Starting SIMULATION in: {path}": "[i] Avvio SIMULAZIONE in: {path}",
    "[!] Starting ORGANIZATION in: {path}": "[!] Avvio ORGANIZZAZIONE in: {path}",
    "Total to move": "Totale da spostare",
    
    # --- CHANGE LANGUAGE ---
    "CHANGE LANGUAGE": "CAMBIA LINGUA",
    "Select language (1-2): ": "Seleziona lingua (1-2): ",
    "Select an option (1-{max_option}): ": "Seleziona un'opzione (1-{max_option}): ",
    "valid_yes": "si",
    "valid_no": "non",
}
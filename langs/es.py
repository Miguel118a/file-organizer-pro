LANGUAGE_NAME = "Español"

MESSAGES = {
    # Months
    1: "Enero", 2: "Febrero", 3: "Marzo", 
    4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre",
    10: "Octubre", 11: "Noviembre", 12: "Diciembre",
    
    # Sizes
    "light": "Ligero",
    "medium": "Mediano",
    "heavy": "Pesado",
    
    # Logger
    "log_movement": "MOVIMIENTO: {file_name} --> {destination}",
    "log_error": "ERROR: Fallo al mover {file_name}. Motivo: {error}",
    "log_cleanup": "LIMPIEZA: Carpeta vacía eliminada --> {folder_name}",
    "log_undo": "UNDO: Reversión completa en {folder}. Archivos devueltos: {amount}",
    
    # Configurator
    "config_error": "[!] Error critico en config.json: {e}",
    "Images": "Imagenes",
    "Media": "Multimedia",
    "Documents": "Documentos",
    "Codes": "Codigos",
    "Compressed": "Comprimidos",
    "Apps": "Programas",
    "Others": "Otros",
    
    # --- Organizer: Errores de Escaneo (scan) ---
    "Error: Path not found {path}": "Error: No se encontró la ruta {path}",
    "Error: You do not have permissions to access {path}": "Error: No tienes permisos para acceder a {path}",
    "Unexpected error while scanning: {e}": "Error inesperado al escanear: {e}",
    "Error during recursive scan: {e}": "Error durante el escaneo recursivo: {e}",
    # --- Organizer: Mensajes de Operación (move/cleanup) ---
    "[i] Cleaning empty directories...": "[i] Limpiando directorios vacíos...",
    
    # --- Organizer: Proceso de Deshacer (undo_movement) ---
    "\n[!] Starting reversion process...": "\n[!] Iniciando proceso de reversión...",
    "[-] Not found: {name}": "[-] No se encontró: {name}",
    "[!] Permission error (file open) in {name}: {e}": "[!] Error de permiso (archivo abierto) en {name}: {e}",
    " [i] Cleanup: Partial copy in root was deleted.": " [i] Limpieza: Se eliminó la copia parcial en la raíz.",
    "[!] Error returning {name}: {e}": "[!] Error devolviendo {name}: {e}",
    
    # Helpers / UI
    "Protected system path: '{path}'": "Ruta de sistema protegida: '{path}'",
    "System folder detected by name: '{name}'": "Carpeta de sistema detectada por nombre: '{name}'",
    "Select a folder": "Seleccione una carpeta",
    "No folder was selected.": "No se seleccionó ninguna carpeta.",
    "Folder not allowed": "Carpeta no permitida",
    "You cannot use this folder as a destination.\n\nMotive: {motive}\n\nPlease select a folder inside your Documents or Desktop.": "No puedes usar esta carpeta como destino.\n\nMotivo: {motive}\n\nSelecciona una carpeta dentro de tus Documentos o Escritorio.",
    "Please enter a number from 1 to {limit}": "Por favor ingrese un número del 1 al {limit}",
    "Only 'yes' or 'no' responses are allowed": "Solo esta permitido responder 'si' o 'no'",
    
    
    # --- Títulos y Opciones del Menú (cli/menu.py) ---
    "FILE ORGANIZER PRO v3.0": "ORGANIZADOR DE ARCHIVOS PRO v3.0",
    "Organize folder": "Organizar carpeta",
    "Simulate organization": "Simular organización",
    "View last summary": "Ver último resumen",
    "Undo last organization": "Deshacer última organización",
    "Change language" : "Cambiar idioma",
    "Exit": "Salir",
    "AVAILABLE CATEGORIES": "CATEGORÍAS DISPONIBLES",
    "Select categories by number separated by comma (e.g.: 1, 2, 3): ": "Seleccione las categorías por número separados por coma (ej: 1, 2, 3): ",
    "is not a valid number. Try again.": "no es un número válido. Intente de nuevo.",
    "Number {num} is out of range. Try again.": "El número {num} está fuera de rango. Intente de nuevo.",
    "ORGANIZATION CRITERIA": "CRITERIOS DE ORGANIZACIÓN",
    "By Date (Year/Month)": "Por Fecha (Año/Mes)",
    "By Type (Image, Document...)": "Por Tipo (Imagen, Documento...)",
    "By Size (Light, Medium, Heavy)": "Por Tamaño (Ligero, Mediano, Pesado)",
    "\nSelect the order of criteria separated by comma (e.g.: 2,1): ": "\nSeleccione el orden de los criterios separados por coma (ej: 2,1): ",
    "is not a valid option.": "no es una opción válida.",
    "Choose category mode:": "Elija el modo de categorías:",
    "All categories": "Todas las categorías",
    "Customize categories": "Personalizar categorías",
    "\nSelect an option (1-2): ": "\nSeleccione una opción (1-2): ",

    # --- Estados y Procesos ---
    "Error: The selected path is no longer available.": "Error: La ruta seleccionada ya no está disponible.",
    "Press Enter to continue...": "Presiona Enter para continuar...",
    "\nDo you want to include subfolders? (yes/no): ": "\n¿Desea incluir subcarpetas? (si/no): ",
    "\nDo you want to delete folders that remain empty after organization? (yes/no): ": "\n¿Desea eliminar las carpetas que queden vacías tras la organización? (si/no): ",
    "Analyzing files and folders...": "Analizando archivos y carpetas...",
    "Organizing, please do not close the program...": "Organizando, por favor no cierre el programa...",
    "Generating preview...": "Generando vista previa...",
    "PREVIEW (SIMULATION)": "VISTA PREVIA (SIMULACIÓN)",
    "Total that would be moved": "Total que se movería",
    "RESULT": "RESULTADO",
    "file(s)": "archivo(s)",
    "Total": "Total",
    "A critical error occurred during the process:": "Ocurrió un error crítico durante el proceso:",
    "Detail": "Detalle",
    "Press Enter to return to the menu...": "Presiona Enter para volver al menú...",

    # --- Historial y Deshacer (Undo) ---
    "LAST EXECUTION": "ÚLTIMA EJECUCIÓN",
    "Folder": "Carpeta",
    "TOTAL MOVED": "TOTAL MOVIDOS",
    "No execution history available.": "No hay historial de ejecuciones disponible.",
    "Perform an organization to generate the first record.": "Realiza una organización para generar el primer registro.",
    "RECOVERY SECTION": "SECCIÓN DE RECUPERACIÓN",
    "Last folder organized": "Última carpeta organizada",
    "Files to return": "Archivos a devolver",
    "\nAre you sure you want to revert these changes? (yes/no): ": "\n¿Seguro que quieres revertir estos cambios? (si/no): ",
    "Process completed!": "¡Proceso completado!",
    "Recovered": "Recuperados",
    "Failed/Not found": "Fallidos/No encontrados",
    "\nDo you want to delete the folders created by the organizer? (yes/no): ": "\n¿Deseas borrar las carpetas creadas por el organizador? (si/no): ",
    "Folder deleted": "Carpeta eliminada",
    "Nothing found to return. Files are no longer there.": "No se encontró nada que devolver. Los archivos ya no están ahí.",
    "Do you want to delete this invalid record from history? (yes/no): ": "¿Deseas eliminar este registro inválido del historial? (si/no): ",
    "Operation canceled.": "Operación cancelada.",
    "No tracking data to undo or history is empty.": "No hay datos de rastreo para deshacer o el historial está vacío.",
    "An error occurred": "Sucedió un error",
    "Are you sure you want to exit the program? (yes/no): ": "¿Estás seguro que deseas salir del programa? (si/no): ",
    # --- app.py: Undo / Reversion ---
    "[!] Reverting last organization in: {folder}": "[!] Revirtiendo última organización en: {folder}",
    "[v] Files returned: {amount}": "[v] Archivos devueltos: {amount}",
    "[v] History and log updated.": "[v] Historial y log actualizados.",
    "[i] Cleaning folders that were created...": "[i] Limpiando carpetas que fueron creadas...",
    "[!] Could not recover any file from '{folder}'.": "[!] No se pudo recuperar ningún archivo de '{folder}'.",
    "[i] Invalid record removed from history.": "[i] Registro inválido eliminado del historial.",
    "[!] No tracking data to undo or history is empty.": "[!] No hay datos de rastreo para deshacer o el historial está vacío.",

    # --- app.py: CLI Errors & Validation ---
    "[!] ERROR: You must specify a path with '-r' to organize.": "[!] ERROR: Debes especificar una ruta con '-r' para organizar.",
    "[!] ERROR: You do not have administrator permissions to move files in this path.": "[!] ERROR: No tienes permisos de administrador para mover archivos en esta ruta.",
    "[!] ERROR: The specified path does not exist.": "[!] ERROR: La ruta especificada no existe.",
    "[!] An unexpected error occurred: {e}": "[!] Ocurrió un error inesperado: {e}",

    # --- app.py: Organization & Simulation ---
    "[i] Starting SIMULATION in: {path}": "[i] Iniciando SIMULACIÓN en: {path}",
    "[!] Starting ORGANIZATION in: {path}": "[!] Iniciando ORGANIZACIÓN en: {path}",
    "Total to move": "Total a mover",
    
    "yes" : "si",
    "no" : "no",
    "valid_yes": "si",
    "valid_no": "no",
    "Select an option (1-6): " : "Seleccione una opción (1-6): ",
    "Select an option (1-{max_option}): " : "Seleccione una opción (1-{max_option}): ",
}
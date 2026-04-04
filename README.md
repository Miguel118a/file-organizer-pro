# File Organizer Pro v3.0

A desktop tool to automatically organize files in any folder. Classifies by type, date, or size, keeps a full history, and lets you undo any operation instantly.

---

## What it does

Takes a folder full of mixed files and moves them into organized subfolders based on the criteria you choose:

- **By type** → Images, Documents, Media, Codes, Compressed, Apps
- **By date** → Year → Month of last modification
- **By size** → Light (< 1MB), Medium (1–100MB), Heavy (> 100MB)
- **Combined** → For example: Type → Date creates `Images/2026/April`

Also includes:
- Preview before moving anything (simulation mode)
- History of the last 10 operations
- **Full undo** — returns every file exactly to where it was
- Automatic log file inside the organized folder
- CLI mode for scripting and automation
- Multi-language support: English, Spanish, Italian (extensible)

---

## Installation

### Option A — Executable (no Python needed)
Download the `FileOrganizerPro` folder from Releases, extract it anywhere, and run `FileOrganizerPro.exe`. No installation required.

### Option B — From source
```bash
git clone https://github.com/Miguel118a/FileOrganizerPro.git
cd FileOrganizerPro
pip install pyinstaller  # only if you want to compile it
python app.py
```
Requires Python 3.10 or higher.

---

## Usage

### Interactive menu
Run without arguments to open the menu:
```bash
python app.py
```

### Command line (CLI)
```bash
# Organize a folder by type
python app.py -r "C:/Users/YOU/Downloads"

# Organize by date and type combined
python app.py -r "C:/Users/YOU/Downloads" -c date type

# Include subfolders
python app.py -r "C:/Users/YOU/Downloads" -rec

# Preview only — no files moved
python app.py -r "C:/Users/YOU/Downloads" -s

# Undo the last organization
python app.py -u

# Delete empty folders when done
python app.py -r "C:/Users/YOU/Downloads" -l yes
```

## Project structure
```text
projecto_versionfinal/
├── app.py                  # Entry point
├── config.json             # Settings and categories (user-editable)
├── history.json            # Auto-generated history file
├── cli/
│   ├── menu.py             # Interactive menu
│   └── helpers.py          # Input utilities and validation
├── core/
│   ├── organizer.py        # Core organization logic
│   ├── estrategy.py        # Classification by type, date, size
│   ├── history.py          # History management
│   ├── configurator.py     # config.json reader
│   └── logger.py           # Operation log writer
├── langs/
│   ├── translator.py       # Translation engine
│   ├── en.py               # English
│   ├── es.py               # Spanish
│   └── it.py               # Italian
└── models/
└── file.py             # File model
```

## Configuration

Open `config.json` to customize behavior:
```json
"settings": {
    "language": "en",
    "default_criteria": ["type"],
    "max_history": 10,
    "ignore": ["log.txt", "config.json", "desktop.ini"]
}
```

To add a new category, add it under `categories`:
```json
"categories": {
    "Design": [".psd", ".ai", ".fig", ".xd", ".sketch"]
}
```

---

## Adding a new language

1. Create `langs/fr.py` by copying the structure of `langs/en.py`
2. Translate all values in the `MESSAGES` dictionary
3. Set `LANGUAGE_NAME = "Français"` at the top of the file
4. The program detects it automatically — it appears in the language change menu

---

## Tech stack

- Python 3.10+
- tkinter — folder selection dialog
- argparse — CLI interface
- json — history and configuration
- shutil / os — file operations

---

## Author

Miguel Gomez — [@Miguel118a](https://github.com/Miguel118a)
Personal project built to practice Python — OOP, file handling, CLI design, and internationalization.



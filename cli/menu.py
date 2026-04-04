from core.organizer import Organizer, Recursive_Organizer
from core.organizer import perform_undo
from core.history import History
from core.configurator import Configurator
from langs.translator import Translator
from cli.helpers import select_path, ask_option, confirm_yes_no
import os


def select_user_categories(total_categories, translator):
    """
    Shows available categories and lets the user choose a subset.
    Validates that the entered numbers are valid before continuing.
    
    Args:
        total_categories: Full dictionary {category: [extensions]}.
        translator: Translator object for i18n.
    Returns a dictionary only with the chosen categories.
    """
    print(f"\n--- {translator.get('AVAILABLE CATEGORIES')} ---")
    category_names = list(total_categories.keys())
    for index, name in enumerate(category_names, start=1):
        print(f"  {index}. {translator.get(name)}")
    print()
    
    while True:
        prompt = translator.get("Select categories by number separated by comma (e.g.: 1, 2, 3): ")
        user_input = input(prompt)
        input_numbers = [n.strip() for n in user_input.split(",")]
        selected_categories = {}
        valid_input = True
        
        for number in input_numbers:
            if not number.isdigit():
                print(f"  '{number}' {translator.get('is not a valid number. Try again.')}\n")
                valid_input = False
                break
            index = int(number) - 1
            if not (0 <= index < len(category_names)):
                print(f"  {translator.get('Number {num} is out of range. Try again.').format(num=number)}\n")
                valid_input = False
                break
            category_name = category_names[index]
            selected_categories[category_name] = total_categories[category_name]
        
        if valid_input and selected_categories:
            return selected_categories

def select_criteria(translator):
    """
    Asks the user to choose and order the organization criteria.
    The order matters: it defines how subfolders are nested.
    Retorna a list of criteria without duplicates in the chosen order.
    """
    print(f"\n--- {translator.get('ORGANIZATION CRITERIA')} ---")
    print(f"1. {translator.get('By Date (Year/Month)')}")
    print(f"2. {translator.get('By Type (Image, Document...)')}")
    print(f"3. {translator.get('By Size (Light, Medium, Heavy)')}")
    
    while True:
        prompt = translator.get("\nSelect the order of criteria separated by comma (e.g.: 2,1): ")
        user_input = input(prompt)
        mapping = {"1": "date", "2": "type", "3": "size"}
        selection = [n.strip() for n in user_input.split(",")]
        final_criteria = []
        valid = True
        
        for s in selection:
            if s in mapping:
                final_criteria.append(mapping[s])
            else:
                print(f"(!) '{s}' {translator.get('is not a valid option.')}")
                valid = False
                break
            
        if valid and final_criteria:
            return list(dict.fromkeys(final_criteria))
    
def show_menu(translator):
    """Clears the screen and shows the main menu."""
    os.system("cls" if os.name == "nt" else "clear")
    print(f'''
    ==========================================
        {translator.get("FILE ORGANIZER PRO v3.0")}
    ==========================================
    1. {translator.get("Organize folder")}
    2. {translator.get("Simulate organization")}
    3. {translator.get("View last summary")}
    4. {translator.get("Undo last organization")}
    5. {translator.get("Change language")}
    6. {translator.get("Exit")}
    ------------------------------------------
    ''')

def select_language(translator):
    """Dynamically displays available languages and lets user choose."""
    import os
    import importlib
    
    langs_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
        "langs"
    )
    
    available_langs = {}
    language_names = {}
    
    # Scan langs/ directory for available language files
    for file in sorted(os.listdir(langs_dir)):
        if file.endswith(".py") and file not in ["__init__.py", "translator.py"]:
            lang_code = file[:-3]
            available_langs[len(available_langs) + 1] = lang_code
            
            # Try to get LANGUAGE_NAME from the module
            try:
                module = importlib.import_module(f"langs.{lang_code}")
                language_names[lang_code] = getattr(module, "LANGUAGE_NAME", lang_code.upper())
            except:
                language_names[lang_code] = lang_code.upper()
    
    # Display available languages
    print(f"\n--- {translator.get('CHANGE LANGUAGE')} ---")
    for idx, lang_code in available_langs.items():
        display_name = language_names.get(lang_code, lang_code.upper())
        print(f"{idx}. {display_name}")
    
    # Get user selection
    max_option = len(available_langs)
    prompt = translator.get("Select an option (1-{max_option}): ", max_option=max_option)
    choice = ask_option(prompt, max_option, translator)
    
    return available_langs[choice]

def run_menu(translator):
    """
    Main loop of the interactive menu.
    Loads configuration once at the start and reuses it.
    """
    # temp_translator = Translator(lang="en")
    # config = Configurator(temp_translator)
    # language = config.get_setting("language", "en")
    
    # if language != temp_translator.lang:
    #     translator = Translator(lang=language)
    #     config = Configurator(translator)

    config = Configurator(translator)

    all_categories = config.get_categories()
    files_to_ignore = config.get_setting("ignore", [])
    max_history = config.get_setting("max_history", 10)
    
    while True:
        show_menu(translator)
        menu_option = ask_option(translator.get("Select an option (1-6): "), 6, translator)
        
        if menu_option in [1, 2]:
            try:
                path = select_path(translator)
                if not path: continue
        
                if not os.path.exists(path):
                    print(translator.get("Error: The selected path is no longer available."))
                    input(translator.get("Press Enter to continue..."))
                    continue
                
                recursive_prompt = translator.get("\nDo you want to include subfolders? (yes/no): ")
                recursive = confirm_yes_no(recursive_prompt, translator)
                
                my_criteria = select_criteria(translator)
                
                print(f"\n{translator.get('Choose category mode:')}\n1. {translator.get('All categories')}\n2. {translator.get('Customize categories')}")
                cat_option = ask_option(f"\n{translator.get('Select an option (1-2): ')}", 2, translator)
                
                final_cats = all_categories
                if cat_option == 2:
                    final_cats = select_user_categories(all_categories, translator)
                    
                clean_prompt = translator.get("\nDo you want to delete folders that remain empty after organization? (yes/no): ")
                clean_empty = confirm_yes_no(clean_prompt, translator)
                
                params = {
                    "path": path,
                    "categories": final_cats,
                    "ignore": files_to_ignore,
                    "criteria": my_criteria,
                    "cleanup": clean_empty,
                    "max_history": max_history,
                    "translator": translator
                }
                
                
                org = Recursive_Organizer(**params) if recursive == "yes" else Organizer(**params)
                
                if menu_option == 1:
                    print(f"\n[i] {translator.get('Analyzing files and folders...')}")
                    print(f"[!] {translator.get('Organizing, please do not close the program...')}")
                    summary = org.move()
                    
                    print(f"\n--- {translator.get('RESULT')} ---")
                    for cat, amount in summary["details"].items():
                        print(f"{translator.get(cat)}: {amount} {translator.get('file(s)')}")
                    print(f"{translator.get('Total')}: {summary['total']}")
                else:
                    print(f"\n[i] {translator.get('Generating preview...')}")
                    sim_summary, sim_total = org.simulate()
                    print(f"\n--- {translator.get('PREVIEW (SIMULATION)')} ---")
                    for folder, files in sim_summary.items():
                        print(f"\n{folder}: {', '.join(files)}")
                    print(f"\n{translator.get('Total that would be moved')}: {sim_total}")
                    
            except Exception as e:
                print(f"\n[!] {translator.get('A critical error occurred during the process:')}")
                print(f"{translator.get('Detail')}: {e}")    
            input(f"\n{translator.get('Press Enter to return to the menu...')}")

        elif menu_option == 3:
            hist = History(max_items=max_history)
            last = hist.get_last()
            if last:
                print("\n" + "="*47)
                print(f"---- {translator.get('LAST EXECUTION')} ({last['date']}) ----")
                print("-" * 13 + f"  {translator.get('Folder')}:{last['folder']}  " + "-" * 13)
                print("-" * 47)
                for cat, amount in last["details"].items():
                    print(f"{translator.get(cat)}: {amount} {translator.get('file(s)')}")
                    print("-" * 40)
                print(f"{translator.get('TOTAL MOVED')}: {last['total']}")
                print("="*47)
            else:
                print(f"\n[!] {translator.get('No execution history available.')}")
                print(translator.get("Perform an organization to generate the first record."))
            input(f"\n{translator.get('Press Enter to return to the menu...')}")
            
        elif menu_option == 4:
            try:
                hist = History(max_items=max_history)
                last = hist.get_last()
                if last and last.get("tracking"):
                    print(f"\n--- {translator.get('RECOVERY SECTION')} ---")
                    print(f"{translator.get('Last folder organized')}: {last['folder']}")
                    print(f"{translator.get('Files to return')}: {last['total']}")
                    
                    undo_prompt = translator.get("\nAre you sure you want to revert these changes? (yes/no): ")
                    confirm = confirm_yes_no(undo_prompt, translator)
                    
                    if confirm == "yes":
                        successes, errors = perform_undo(last, hist, translator)
                        print("-" * 30)
                        print(f"[v] {translator.get('Process completed!')}")
                        if successes > 0:
                            print(f" -> {translator.get('Recovered')}: {successes}")
                            if errors > 0:
                                print(f" -> {translator.get('Failed/Not found')}: {errors}")
                                
                            if last.get("new_folders"):
                                delete_prompt = translator.get("\nDo you want to delete the folders created by the organizer? (yes/no): ")
                                delete_f = confirm_yes_no(delete_prompt, translator)
                                
                                if delete_f == "yes":
                                    for folder_path in reversed(last["new_folders"]):
                                        current_path = os.path.normpath(folder_path)
                                        root_path = os.path.normpath(os.path.join(os.path.dirname(last["tracking"][0]["origin"])))

                                        while current_path != root_path:
                                            if os.path.exists(current_path) and not os.listdir(current_path):
                                                os.rmdir(current_path)
                                                print(f" -> {translator.get('Folder deleted')}: {os.path.basename(current_path)}")
                                                current_path = os.path.dirname(current_path)
                                            else:
                                                break
                        else: 
                            print(f"\n[!] {translator.get('Nothing found to return. Files are no longer there.')}")
                            ghost_prompt = translator.get("Do you want to delete this invalid record from history? (yes/no): ")
                            delete_ghost = confirm_yes_no(ghost_prompt, translator)
                            if delete_ghost == "yes":
                                hist.delete_last()
                    else:
                        print(f"\n[i] {translator.get('Operation canceled.')}")
                else:
                    print(f"\n[!] {translator.get('No tracking data to undo or history is empty.')}")
                input(f"\n{translator.get('Press Enter to return to the menu...')}")
                
            except Exception as e:
                print(f"{translator.get('An error occurred')}: {e}")
                input(f"\n{translator.get('Press Enter to return to the menu...')}")
                
        elif menu_option == 5:
            new_lang = select_language(translator)
            translator = Translator(lang=new_lang)
            config = Configurator(translator)
            config.set_setting("language", new_lang)
        else:
            exit_prompt = translator.get("Are you sure you want to exit the program? (yes/no): ")
            exit_op = confirm_yes_no(exit_prompt, translator)
            if exit_op == "yes":
                break
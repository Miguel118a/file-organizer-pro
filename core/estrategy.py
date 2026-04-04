import os
from datetime import datetime

def get_by_type(file_obj, config_types, translator):
    """
    Returns the folder name based on the file extension.
    If it doesn't match any category, returns a translated "Others".
    
    Args: 
        file_obj: File object.
        config_types: Dictionary: {category: [extensions]} from config.json.
        translator: Translator object for i18n.
    """
    for category, extensions in config_types.items():
        if file_obj.extension.lower() in extensions:
            return translator.get(category)
    return translator.get("Others")


def get_by_date(file_obj, translator):
    """
    Returns the 'Year/Month' path based on the file's modification date.
    
    Args:
        file_obj: File object.
        translator: Translator object for i18n.
    """
    file_time = os.path.getmtime(file_obj.full_path)
    date_val = datetime.fromtimestamp(file_time)
    year = str(date_val.year)
    month_name = translator.get(date_val.month)
    return os.path.join(year, month_name)
    
    
def get_by_size(file_obj, translator):
    """
    Returns "light", "medium" or "heavy" (translated) based on file size.
    
    Args:
        file_obj: File object.
        translator: Translator object for i18n.
    """
    file_bytes = os.path.getsize(file_obj.full_path)
    size_mb = file_bytes / (1024*1024)
    if size_mb < 1:
        return translator.get("light")
    elif 1 <= size_mb <= 100:
        return translator.get("medium")
    else:
        return translator.get("heavy")
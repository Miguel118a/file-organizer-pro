import importlib

class Translator:
    """
    Handles multi-language support for the file organizer.
    """
    def __init__(self, lang="en"):
        self.lang = lang
        try:
            module = importlib.import_module(f"langs.{lang}")
            self.messages = module.MESSAGES
        except ImportError:
            self.messages = {}  # Fallback to empty if module not found

    def get(self, key, **kwargs):
        """
        Retrieves and formats a translated message.
        
        Args:
            key: The message key.
            **kwargs: Variables to format in the message.
        
        Returns:
            The translated and formatted message, or the key if not found.
        """
        try:
            text = self.messages.get(key, key)
            return text.format(**kwargs)
        except KeyError:
            print(f"[Translator] Missing variable for key '{key}': {kwargs}")
            return text            
import json


class TranslationManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.translations = {}
            TranslationManager._initialized = True

    def load_translations(self, file: str):
        # Resolve the path to translations.json
        with open(file, "r", encoding="utf-8") as f:
            self.translations.update(json.load(f))
        print("Translations loaded into memory.")

    def tm(self, key: str, **kwargs) -> str:
        """
        Retrieve a translation by key, supporting nested keys using dot notation.
        Example: "reception.has_booking"
        """
        keys = key.split(".")  # Split the key by dots
        current_level = self.translations  # Start at the root of the translations

        # Traverse the nested structure
        for k in keys:
            if k in current_level:
                current_level = current_level[k]
            else:
                # Key not found, return the original key
                return key

        # If the final value is a string, format it with kwargs
        if isinstance(current_level, str):
            try:
                return current_level.format(**kwargs)
            except KeyError:
                return current_level
        else:
            # If the final value is not a string (e.g., a nested object), return the key
            return key


# Create a singleton instance
translation_manager = TranslationManager()
tm = translation_manager.tm

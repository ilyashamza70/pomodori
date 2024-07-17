# cli/settings.py
from models.settings import Settings

def load_settings():
    settings = Settings.load()
    print(f"Loaded settings: {settings}")

def save_settings():
    settings = Settings()
    settings.save()
    print("Saved settings.")

# cli/settings.py
from models.settings import Settings

def load_settings():
    """
    Carica le impostazioni dal file di configurazione.

    Returns:
        Settings: Un'istanza della classe Settings con le impostazioni caricate.
    """
    settings = Settings.load()
    print(f"Loaded settings: {settings}")
    return settings

def save_settings():
    """
    Salva le impostazioni correnti nel file di configurazione.

    Returns:
        None
    """
    settings = Settings()
    settings.save()
    print("Saved settings.")

def get_settings():
    """
    Ottiene le impostazioni correnti.

    Returns:
        Settings: Un'istanza della classe Settings con le impostazioni correnti.
    """
    return Settings.load()

def update_settings(**kwargs):
    """
    Aggiorna le impostazioni con i valori forniti.

    Args:
        **kwargs: Coppie chiave-valore delle impostazioni da aggiornare.

    Returns:
        None
    """
    settings = Settings.load()
    for key, value in kwargs.items():
        if hasattr(settings, key):
            setattr(settings, key, value)
            print(f"Updated {key} to {value}")
        else:
            print(f"Setting {key} does not exist.")
    settings.save()
    print("Settings updated and saved.")

def reset_settings():
    """
    Resetta le impostazioni ai valori di default.

    Returns:
        None
    """
    settings = Settings.default()
    settings.save()
    print("Settings have been reset to default values.")

def display_settings():
    """
    Visualizza le impostazioni correnti in modo leggibile.

    Returns:
        None
    """
    settings = Settings.load()
    print("Current settings:")
    for key, value in settings.__dict__.items():
        print(f"{key}: {value}")

# Esempio di utilizzo delle nuove funzioni
if __name__ == "__main__":
    # Carica le impostazioni
    load_settings()

    # Aggiorna alcune impostazioni
    update_settings(theme="dark", notifications=True)

    # Visualizza le impostazioni aggiornate
    display_settings()

    # Resetta le impostazioni ai valori di default
    reset_settings()

    # Visualizza le impostazioni resettate
    display_settings()
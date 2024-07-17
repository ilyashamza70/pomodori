# models/settings.py
class Settings:
    def __init__(self):
        self.theme = 'light'
        self.timers = {'work': 45, 'short_break': 15, 'long_break': 60}
        self.background_image = ''
        self.font = 'default'

    @classmethod
    def load(cls):
        # Load settings from file or database
        return cls()

    def save(self):
        # Save settings to file or database
        pass

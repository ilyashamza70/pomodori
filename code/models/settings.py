# models/settings.py
import json
import os

class Settings:
    def __init__(self):
        self.theme = 'light'
        self.timers = {'work': 45, 'short_break': 15, 'long_break': 75}
        self.background_image = ''
        self.font = 'default'

    @classmethod
    def load(cls, filepath='settings.json'):
        # Load settings from a JSON file
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
                settings = cls()
                settings.theme = data.get('theme', 'light')
                settings.timers = data.get('timers', {'work': 45, 'short_break': 15, 'long_break': 75})
                settings.background_image = data.get('background_image', '')
                settings.font = data.get('font', 'default')
                return settings
        else:
            return cls()

    def save(self, filepath='settings.json'):
        # Save settings to a JSON file
        data = {
            'theme': self.theme,
            'timers': self.timers,
            'background_image': self.background_image,
            'font': self.font
        }
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def get_default_settings():
        return {
            'theme': 'dark',
            'timers': {'work': 45, 'short_break': 15, 'long_break': 75},
            'background_image': '',
            'font': 'default'
        }
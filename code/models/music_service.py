# models/music_service.py
class MusicService:
    def __init__(self, service_name):
        self.service_name = service_name
        self.connected = False
        self.current_playlist = ''

    def connect(self, service_name):
        self.service_name = service_name
        self.connected = True
        print(f"Connected to {service_name}")

    def play_music(self, playlist):
        if self.connected:
            self.current_playlist = playlist
            print(f"Playing music from {playlist}")

    def pause_music(self):
        if self.connected:
            print("Music paused")

    def stop_music(self):
        if self.connected:
            self.current_playlist = ''
            print("Music stopped")

# models/user.py
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.local_data = {}
        self.remote_data = {}

    def login(self, username, password):
        # Login logic here
        pass

    def logout(self):
        # Logout logic here
        pass

    def save_data_locally(self):
        # Save data locally
        pass

    def sync_data(self):
        # Sync data with remote server
        pass

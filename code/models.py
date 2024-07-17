from datetime import datetime

class PomodoroSession:
    def __init__(self, task, duration):
        self.task = task
        self.duration = duration
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()
        # Here, you would log the session to a database

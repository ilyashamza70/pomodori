# models/pomodoro_session.py
from datetime import datetime

class PomodoroSession:
    current_session = None

    def __init__(self, task, duration, start_time=None):
        self.task = task
        self.duration = duration
        self.start_time = start_time or datetime.now()
        self.end_time = None
        self.completed = False

    def start(self):
        PomodoroSession.current_session = self
        print(f"Session started: {self.task} for {self.duration} minutes.")

    def end(self):
        self.end_time = datetime.now()
        self.completed = True
        PomodoroSession.current_session = None
        print(f"Session ended: {self.task}.")

    @classmethod
    def end_current(cls):
        if cls.current_session:
            cls.current_session.end()

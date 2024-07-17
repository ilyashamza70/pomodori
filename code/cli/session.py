# cli/session.py
from datetime import datetime
from models.pomodoro_session import PomodoroSession

current_session = None

def start_session(task, duration):
    global current_session
    if current_session is None or current_session.is_complete():
        current_session = PomodoroSession(task, duration, datetime.now())
        print(f"Started session: {task} for {duration} minutes.")
    else:
        print("There is already an ongoing session.")

def end_session():
    global current_session
    if current_session and not current_session.is_complete():
        current_session.end()
        print(f"Ended session: {current_session.task}.")
    else:
        print("No ongoing session to end.")

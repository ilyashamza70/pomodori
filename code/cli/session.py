# cli/session.py
import json
import os

SESSION_FILE = 'current_session.json'
HISTORY_FILE = 'session_history.json'

def start_session(task, duration):
    session = {
        'task': task,
        'duration': duration,
        'status': 'active'
    }
    with open(SESSION_FILE, 'w') as f:
        json.dump(session, f)
    print(f"Started session: {task} for {duration} minutes.")

def end_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            session = json.load(f)
        session['status'] = 'completed'
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
        else:
            history = []
        history.append(session)
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f)
        os.remove(SESSION_FILE)
        print("Ended the current Pomodoro session.")
    else:
        print("No ongoing session to end.")

def get_current_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return None

def get_session_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def display_current_session(session):
    print(f"Current session: {session['task']} for {session['duration']} minutes.")

def display_session_history(history):
    for session in history:
        print(f"Task: {session['task']}, Duration: {session['duration']} minutes, Status: {session['status']}")

# cli/main.py
import click
from cli.session import start_session, end_session, get_current_session, get_session_history, display_current_session, display_session_history

@click.group()
def cli():
    """Pomodoro CLI Application"""
    pass

@cli.command()
@click.argument('task')
@click.argument('duration', type=int)
def start(task, duration):
    start_session(task, duration)
    click.echo(f"Started Pomodoro session for task '{task}' with duration {duration} minutes.")

@cli.command()
def end():
    end_session()
    click.echo("Ended the current Pomodoro session.")

@cli.command()
def status():
    session = get_current_session()
    if session:
        display_current_session(session)
    else:
        click.echo("No active Pomodoro session.")

@cli.command()
def history():
    history = get_session_history()
    if history:
        display_session_history(history)
    else:
        click.echo("No Pomodoro session history available.")

if __name__ == "__main__":
    cli()
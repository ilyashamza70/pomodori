# cli/session.py
import json
import os
import csv
from datetime import datetime
from models.settings import Settings

# Carica le impostazioni se ci sono, altrimenti usa default GRIND master
settings = Settings.load()
# Utilizza le impostazioni
PRESET_DURATION = settings.timers['work']

SESSION_FILE = 'current_session.json'
HISTORY_FILE = 'session_history.csv'

# cli/session.py
def start_session_Grind(task, duration, cycles=4, short_break=15, long_break=75, use_breaks=True):
    """
    Avvia una sessione Pomodoro con i parametri forniti.

    Args:
        task (str): Il compito da svolgere durante la sessione.
        duration (int): La durata della sessione in minuti.
        cycles (int): Il numero di cicli Pomodoro.
        short_break (int): La durata della pausa breve in minuti.
        long_break (int): La durata della pausa lunga in minuti.
        use_breaks (bool): Se utilizzare le pause o meno.
    """
    print(f"Starting session: {task}, Duration: {duration}, Cycles: {cycles}, Short Break: {short_break}, Long Break: {long_break}, Use Breaks: {use_breaks}")
    # Aggiungi qui la logica per gestire la cronologia se necessario
    # Implementa la logica per avviare una sessione Pomodoro con i parametri forniti
    print(f"Starting session: {task}, Duration: {duration}, Cycles: {cycles}, Short Break: {short_break}, Long Break: {long_break}, Use Breaks: {use_breaks}")
    # Aggiungi qui la logica per gestire la cronologia se necessario


def start_session(task, duration):
    start_time = datetime.now().isoformat()
    session = {
        'task': task,
        'duration': duration,
        'status': 'active',
        'start_time': start_time,
        'end_time': None
    }
    with open(SESSION_FILE, 'w') as f:
        json.dump(session, f)
    print(f"Started session: {task} for {duration} minutes.")

def get_start_time(task):
    return task['start_time']

def get_time_remaining(task):
    start_time = datetime.fromisoformat(task['start_time'])
    duration = task['duration']
    elapsed_time = (datetime.now() - start_time).total_seconds() / 60
    time_remaining = duration - elapsed_time
    return time_remaining
def end_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            session = json.load(f)
        end_time = datetime.now().isoformat()
        session['end_time'] = end_time
        elapsed_time = (datetime.fromisoformat(end_time) - datetime.fromisoformat(session['start_time'])).total_seconds() / 60
        if elapsed_time >= session['duration']:
            session['status'] = 'completed'
        else:
            session['status'] = 'ended earlier'
        
        # Append session to CSV history file
        file_exists = os.path.isfile(HISTORY_FILE)
        with open(HISTORY_FILE, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=session.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(session)
        
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
            reader = csv.DictReader(f)
            return list(reader)
    return []

def display_current_session(session):
    print(f"Current session: {session['task']} for {session['duration']} minutes.")
    print(f"Started at: {session['start_time']}")

def display_session_history(history):
    for session in history:
        print(f"Task: {session['task']}, Duration: {session['duration']} minutes, Status: {session['status']}, Start Time: {session['start_time']}, End Time: {session['end_time']}")

# cli/main.py
import click
from cli.session import start_session, end_session, get_current_session, get_session_history, display_current_session, display_session_history

@click.group()
def cli():
    """Pomodoro CLI Application"""
    pass

@cli.command()
@click.argument('task', default='GRIND')  # Imposta il task predefinito a 'GRIND'
def start(task):
    duration = PRESET_DURATION  # Usa la durata preimpostata
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
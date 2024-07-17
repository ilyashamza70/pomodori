# cli/main.py
import click
from cli.session import start_session, end_session, get_current_session, get_session_history, display_current_session, display_session_history
from cli.settings import load_settings, save_settings, get_settings, display_settings

@click.group()
def cli():
    """Pomodoro CLI Application"""
    pass

@cli.command()
@click.argument('task')
@click.argument('duration', type=int)
def start(task, duration):
    """
    Start a Pomodoro session with a specified TASK and DURATION (in minutes).

    Args:
        task (str): The task to be performed during the session.
        duration (int): The duration of the session in minutes.
    """
    start_session(task, duration)
    click.echo(f"Started Pomodoro session for task '{task}' with duration {duration} minutes.")

@cli.command()
def end():
    """
    End the current Pomodoro session.
    """
    end_session()
    click.echo("Ended the current Pomodoro session.")

@cli.command()
def status():
    """
    Display the status of the current Pomodoro session.
    """
    session = get_current_session()
    if session:
        display_current_session(session)
    else:
        click.echo("No active Pomodoro session.")

@cli.command()
def history():
    """
    Display the history of Pomodoro sessions.
    """
    history = get_session_history()
    if history:
        display_session_history(history)
    else:
        click.echo("No Pomodoro session history available.")

@cli.command()
def interrupt():
    """
    Interrupt the current Pomodoro session.
    """
    session = get_current_session()
    if session:
        end_session()
        click.echo("Interrupted the current Pomodoro session.")
    else:
        click.echo("No ongoing session to interrupt.")

@cli.command()
def show_settings():
    """
    Display the current settings.
    """
    settings = get_settings()
    if settings:
        display_settings()
    else:
        click.echo("No settings available.")

@cli.command()
def settings():
    """
    Load and save settings.
    """
    load_settings()
    save_settings()
    click.echo("Settings loaded and saved.")

if __name__ == "__main__":
    cli()
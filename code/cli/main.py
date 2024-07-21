import click
from cli.session import (
    start_session_Grind, start_session, end_session, get_current_session, get_session_history,
    display_current_session, display_session_history, get_start_time, get_time_remaining
)
from cli.settings import load_settings, save_settings, get_settings, display_settings

DEFAULT_TASK = 'GRIND'
DEFAULT_DURATION = 45
DEFAULT_CYCLES = 4
DEFAULT_SHORT_BREAK = 15
DEFAULT_LONG_BREAK = 75
DEFAULT_USE_BREAKS = True

@click.group()
def cli():
    """Pomodoro CLI Application"""
    pass


@cli.command()
@click.argument('task', required=False, default=DEFAULT_TASK)
@click.argument('duration', type=int, required=False, default=DEFAULT_DURATION)
def start(task, duration):
    """
    Start a Pomodoro session with a specified TASK and DURATION (in minutes).
    If not arguments are given the default GRIND settings should be activated:
    - task: GRIND features:
        - duration: 45 minutes
        - cycles: 4
        - short_break: 15 minutes
        - long_break: 75 minutes
        - use_breaks: True
        
    Args:
        task (str): The task to be performed during the session. 
            If none is given GRIND is activated
        duration (int): The duration of the session in minutes.
    """
    if task == DEFAULT_TASK and duration == DEFAULT_DURATION:
        # Use default GRIND settings
        start_session_Grind(task, duration, DEFAULT_CYCLES, DEFAULT_SHORT_BREAK, DEFAULT_LONG_BREAK, DEFAULT_USE_BREAKS)
    else:
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
        start_time = get_start_time(session)
        time_remaining = get_time_remaining(session)
        click.echo(f"Start time: {start_time}")
        click.echo(f"Time remaining: {time_remaining} minutes")
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
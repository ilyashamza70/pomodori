# cli/main.py
import click
from cli.session import start_session, end_session
from cli.settings import load_settings, save_settings

@click.group()
def cli():
    """Pomodoro CLI Application"""
    pass

@cli.command()
@click.argument('task')
@click.argument('duration', type=int)
def start(task, duration):
    """Start a Pomodoro session"""
    start_session(task, duration)

@cli.command()
def end():
    """End the current Pomodoro session"""
    end_session()

@cli.command()
def settings():
    """Load and save settings"""
    load_settings()
    save_settings()

if __name__ == '__main__':
    cli()

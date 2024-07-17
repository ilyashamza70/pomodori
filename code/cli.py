import time
from code.utils import notify
from models import PomodoroSession

def start_pomodoro(task, duration):
    session = PomodoroSession(task, duration)
    session.start()
    notify("Pomodoro started for task: " + task)
    time.sleep(duration * 60)
    session.end()
    notify("Pomodoro session ended for task: " + task)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Pomodoro CLI")
    parser.add_argument("command", choices=["start", "end"], help="Command to run")
    parser.add_argument("--task", help="Task description")
    parser.add_argument("--duration", type=int, help="Duration in minutes")

    args = parser.parse_args()

    if args.command == "start":
        if not args.task or not args.duration:
            print("Task and duration are required for start command")
            return
        start_pomodoro(args.task, args.duration)
    elif args.command == "end":
        print("End command not implemented yet")

if __name__ == "__main__":
    main()

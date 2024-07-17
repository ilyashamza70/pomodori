# web/app.py
from flask import Flask, render_template, request, redirect, url_for
from models.pomodoro_session import PomodoroSession
from models.settings import Settings
from models.user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_session', methods=['POST'])
def start_session():
    task = request.form.get('task')
    duration = int(request.form.get('duration'))
    session = PomodoroSession(task, duration)
    session.start()
    return redirect(url_for('index'))

@app.route('/end_session')
def end_session():
    PomodoroSession.end_current()
    return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Save settings logic here
        pass
    settings = Settings.load()
    return render_template('settings.html', settings=settings)

@app.route('/statistics')
def statistics():
    # Load statistics logic here
    return render_template('statistics.html')

if __name__ == '__main__':
    app.run(debug=True)

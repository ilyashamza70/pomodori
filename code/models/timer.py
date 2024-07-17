# models/timer.py
class Timer:
    def __init__(self, work_duration, short_break_duration, long_break_duration, sessions_before_long_break):
        self.work_duration = work_duration
        self.short_break_duration = short_break_duration
        self.long_break_duration = long_break_duration
        self.sessions_before_long_break = sessions_before_long_break

    def set_work_duration(self, duration):
        self.work_duration = duration

    def set_short_break_duration(self, duration):
        self.short_break_duration = duration

    def set_long_break_duration(self, duration):
        self.long_break_duration = duration

    def set_sessions_before_long_break(self, sessions):
        self.sessions_before_long_break = sessions

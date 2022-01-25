import time
import json


class Timer:
    def __init__(self, user_timeshift=600):
        self.time_executed = 0.0
        self.time_shift = user_timeshift
        self.count_shifts = 0
        self.is_polling = True
        self.timers = 0

    def polling(self):
        if not self.is_polling:
            return
        self.time_executed += 0.5

    def shift_check(self):
        if self.time_executed // self.time_shift > self.count_shifts:
            self.count_shifts += 1
            return True
        else:
            return False

    def executed(self):
        return self.time_executed

    def change_shift(self, new_time_shift):
        self.time_shift = new_time_shift

    def end_timer(self):
        self.is_polling = False

    @staticmethod
    def format_time(secs):
        return f'{int(secs//3600):02d}:{int(secs//60 % 60):02d}:{int(secs % 60):02d}'

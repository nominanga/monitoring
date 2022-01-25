import win32process
import psutil
import win32gui

from timer import Timer


class AppActivity(Timer):
    def __init__(self, user_timeshift):
        super().__init__(user_timeshift)
        self.window = win32gui.GetForegroundWindow()
        #self.saved_windows = []
        self.prev_window = self.window

    def opened(self):
        self.window = win32gui.GetForegroundWindow()
        if self.prev_window != self.window:
            self.prev_window = self.window
            self.time_executed = 0.0
            #if self.window in self.saved_windows:
             #   pass
            #else:
            #    self.saved_windows.append(self.window)
        pid = win32process.GetWindowThreadProcessId(self.window)
        proc = psutil.Process(pid[-1])
        return [proc.name(), win32gui.GetWindowText(self.window)]

    # def cpu_usage(self):
    #     self.window = win32gui.GetForegroundWindow()
    #     pid = win32process.GetWindowThreadProcessId(self.window)
    #     proc = psutil.Process(pid[-1])
    #     return f'CPU: {proc.cpu_percent(0.001)/2}%, RAM: {proc.memory_percent()}%'


import win32api
import keyboard as key
import threading


class UserActivity:
    def __init__(self):
        self.left_state = win32api.GetKeyState(0x01)
        self.right_state = win32api.GetKeyState(0x02)
        self.cursor_state = win32api.GetCursorPos()
        self.count_click = 0
        self.count_movement = 0
        self.key_state = key.read_key()
        self.count_press = 0

    def mouse_click_check(self):
        left_clicked = win32api.GetKeyState(0x01)
        right_clicked = win32api.GetKeyState(0x02)
        if left_clicked != self.left_state:
            self.left_state = left_clicked
            if left_clicked < 0:
                self.count_click += 1

        if right_clicked != self.right_state:
            self.right_state = right_clicked
            if right_clicked < 0:
                self.count_click += 1

    def keyboard_click_check(self):
        key_clicked = key.read_key()
        if key_clicked != self.key_state:
            self.key_state = key_clicked
            if key_clicked != '':
                self.count_press += 1

    def mouse_movement_check(self):
        pos = win32api.GetCursorPos()
        if self.cursor_state != pos:
            self.count_movement += 1
            self.cursor_state = pos

    def get_stats(self):
        return self.count_click // 1.4 + self.count_movement // 8 + self.count_press

    def reset(self):
        self.count_movement = 0
        self.count_click = 0

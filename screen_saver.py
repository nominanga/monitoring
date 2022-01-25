import pyautogui
from os import listdir


class PrtScr:
	def __init__(self):
		self.count_files = len(listdir('media/'))
		self.path = f"media/screenshot({self.count_files}).png"
		self.screenshots_count = 0

	def take_shot(self):
		if self.screenshots_count >= 2:
			return
		screen = pyautogui.screenshot()
		screen.save(self.path)
		self.screenshots_count += 1
		self.count_files += 1
		self.path = f"media/screenshot({self.count_files}).png"

	def reset_count(self):
		self.screenshots_count = 0


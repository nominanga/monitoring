from time import sleep
from random import randint
import threading

from cpu import AppActivity
from mouse_check import UserActivity
from screen_saver import PrtScr
from timer import Timer

time_shift = 600

data = {
    "timer":{
        "number": 
    }
}

timer = Timer(time_shift)
stats = UserActivity()
app = AppActivity(time_shift)
shots_handler = PrtScr()
seconds_for_scr = [randint(1, time_shift // 2), randint(time_shift//2+1, time_shift)]

def for_app(app=app):
    app.polling()
    #app.executed()
    #print(app.opened())

def for_timer(timer=timer):
    global stats, shots_handler, app, seconds_for_scr
    timer.polling()

    if timer.shift_check():
        seconds_for_scr = [randint(1, time_shift // 2), randint(time_shift//2+1, time_shift)]
        rates = stats.get_stats() / timer.time_shift
        print(f'{100 if rates > 1 else rates*100}%')
        stats.reset()
        shots_handler.reset_count()
        seconds_for_scr = [randint(1, time_shift // 2), randint(time_shift//2+1, time_shift)]

def mouse_keyboard(stats=stats):
    stats.mouse_movement_check()
    stats.mouse_click_check()
    stats.keyboard_click_check()

def taking_shot(shots_handler=shots_handler):
    global timer, seconds_for_scr
    for i in range(len(seconds_for_scr)):
        print(seconds_for_scr[i])
        if int(timer.executed() % timer.time_shift) == seconds_for_scr[i]:
            seconds_for_scr[i] = -1
            shots_handler.take_shot()


def main():


    while True:

        timer_thread = threading.Thread(target=for_timer)
        timer_thread.start()
        app_thread = threading.Thread(target=for_app)
        app_thread.start()
        activity = threading.Thread(target=mouse_keyboard)
        activity.start()
        shot = threading.Thread(target=taking_shot)
        shot.start()





        sleep(0.5)


if __name__ == '__main__':
    main()

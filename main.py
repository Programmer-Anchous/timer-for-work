import time
from shell_functions import clear
from playsound import playsound
import subprocess


def start_work():
    subprocess.run(["notify-send", "Timer", "work"])


def start_break():
    subprocess.run(["notify-send", "Timer", "Break"])


class Clock:
    def __init__(self):
        self.time_prev = time.time()
        self.time_counter = 0

    def tick(self):
        time.sleep(1 - (time.time() - self.time_prev))
        self.time_prev = time.time()


class Canvas:
    def __init__(self):
        self.timers = [
            [25, "first session", 0],
            [5, "first break", 1],
            [25, "second session", 0],
            [5, "second break", 1],
            [25, "third session", 0],
            [5, "third break", 1],
            [25, "fourth session", 0],
            [25, "big break", 1]
        ]
        self.timer_limit = len(self.timers)
        self.current_timer = 0
        self.clock = Clock()
        self.current = 0

    def start(self):
        start_work()
        while True:
            self.current += 1
            if self.current >= self.timers[self.current_timer][0] * 60:
                self.current = 0
                self.current_timer += 1
                if self.current_timer >= self.timer_limit:
                    self.current_timer = 0

                if self.timers[self.current_timer][2] == 0:
                    start_work()
                else:
                    start_break()
            self.information()
            self.clock.tick()

    def information(self):
        timer_time, timer_text = self.timers[self.current_timer][:2]
        remained = timer_time * 60 - self.current
        minutes = str(remained // 60).rjust(2, '0')
        seconds = str(remained % 60).rjust(2, '0')
        clear()
        print(f"   {timer_text}")
        print(f"{timer_time} minutes")
        print(f"{minutes}:{seconds}")


time.sleep(1)
canvas = Canvas()
canvas.start()

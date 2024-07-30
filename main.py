import time

from shell_functions import clear_screen
from tg_message import send_message


def start_work(message):
    send_message(f"work: {message}")


def start_break(message):
    send_message(f"{message}")


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
            {"minutes": 25, "message": "first session", "is_work": True},
            {"minutes": 5, "message": "first break", "is_work": False},
            {"minutes": 25, "message": "second session", "is_work": True},
            {"minutes": 5, "message": "second break", "is_work": False},
            {"minutes": 25, "message": "third session", "is_work": True},
            {"minutes": 5, "message": "third break", "is_work": False},
            {"minutes": 25, "message": "fourth session", "is_work": True},
            {"minutes": 25, "message": "big break", "is_work": False}
        ]
        self.timer_limit = len(self.timers)
        self.current_timer = 0
        self.clock = Clock()
        self.current = 0

    def start(self):
        start_work(self.timers[self.current_timer]["message"])
        while True:
            self.current += 1
            if self.current >= self.timers[self.current_timer]["minutes"] * 60:
                self.current = 0
                self.current_timer += 1
                if self.current_timer >= self.timer_limit:
                    self.current_timer = 0

                if self.timers[self.current_timer]["is_work"] == 1:
                    start_work(self.timers[self.current_timer]["message"])
                else:
                    start_break(self.timers[self.current_timer]["message"])
            self.information()
            self.clock.tick()

    def information(self):
        timer_time = self.timers[self.current_timer]["minutes"]

        seconds_remained = timer_time * 60 - self.current
        minutes = str(seconds_remained // 60).rjust(2, '0')

        seconds = str(seconds_remained % 60).rjust(2, '0')
        clear_screen()

        print(f"{' ' * 25} left | total")
        offset = 12
        for i, timer_info in enumerate(self.timers):
            message = timer_info["message"]

            if i == self.current_timer:
                whitespaces = (offset - len(message) // 2 - 2) * ' '
                timer_name = whitespaces + f"< {message} >"

                print(
                    (timer_name).ljust(24, " "),
                    f"{minutes}:{seconds}",
                    f"| {timer_info["minutes"]} min"
                )
            else:
                whitespaces = (offset - len(message) // 2) * ' '
                timer_name = whitespaces + f"{message}"
                print(
                    (timer_name).ljust(30, " "),
                    f"| {timer_info["minutes"]} min"
                )

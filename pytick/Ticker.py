import time


class Ticker:
    def __init__(self, tick_interval_s):
        self.tick_interval = tick_interval_s
        self.counter = 0

    def start(self):
        self.last_tick_time = time.time()

    def update(self) -> tuple[bool, int]:
        now = time.time()
        elapsed_t = now - self.last_tick_time
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now

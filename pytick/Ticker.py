import time


class Ticker:
    def __init__(self, tick_interval_s):
        self.tick_interval = tick_interval_s
        self.counter = 0
        self.last_tick_time = None
        self.block = False

    def start(self):
        self.last_tick_time = time.time()

    def update(self) -> tuple[bool, int]:
        now = time.time()
        elapsed_t = now - self.last_tick_time
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now

    def counter_comp(self, mod):
        if self.counter % mod == 0 and self.block is False:
            self.block = True
            return True
        else:
            self.block = False
            return False

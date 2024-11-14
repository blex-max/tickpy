import time


class Ticker:
    def __init__(self, tick_interval_s):
        self.tick_interval = tick_interval_s
        self.counter = 0
        self.last_tick_time = None
        self.__block_flags = {}

    def start(self):
        self.last_tick_time = time.time()

    def update(self) -> tuple[bool, int]:
        now = time.time()
        elapsed_t = now - self.last_tick_time
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now

    def counter_comp(self, mod):
        try:
            self.__block_flags[mod]
        except KeyError:
            self.__block_flags[mod] = None
        if self.counter % mod == 0:
            if not self.__block_flags[mod]:
                self.__block_flags[mod] = True
                return True
        if self.counter % mod != 0 and self.__block_flags[mod]:
            self.__block_flags[mod] = False
        return False

import time


class Ticker:
    def __init__(self, tick_interval_s):
        self.tick_interval = tick_interval_s
        self.counter = 0
        self.last_tick_time = None
        self.started = False
        self.__block_flags = {}

    def start(self):
        self.last_tick_time = time.time()
        self.started = True

    def update(self) -> tuple[bool, int]:
        if not self.started:
            raise RuntimeError('ticker not started, call .start() before use')
        now = time.time()
        elapsed_t = now - self.last_tick_time
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now
        for k in self.__block_flags:
            if self.counter % k != 0 and self.__block_flags[k]:
                self.__block_flags[k] = False

    def counter_comp(self,
                     mod,
                     chk: bool = True,
                     blk: bool = True,
                     unblk: bool = True):
        try:
            self.__block_flags[mod]
        except KeyError:
            self.__block_flags[mod] = None
        if self.counter % mod == 0:
            # falls through to final return False
            if chk and not self.__block_flags[mod]:
                if blk:
                    self.__block_flags[mod] = True
                return True
            elif not chk:
                if blk and not self.__block_flags[mod]:
                    self.__block_flags[mod] = True
                return True
        # could tie yourself in knots here, fragile
        if self.counter % mod != 0 and self.__block_flags[mod] and unblk:
            self.__block_flags[mod] = False
        return False

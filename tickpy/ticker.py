from time import perf_counter


class MinTicker:
    def __init__(self,
                 tick_interval_s: float):
        self.tick_interval = tick_interval_s
        self.counter: int = 0
        self.start_time = perf_counter()

    def update(self):
        prev = self.counter
        self.counter = int((perf_counter() - self.start_time) / self.tick_interval)
        return True if self.counter != prev else False


    def mod(self,
            mod: int):
        if self.counter % mod == 0:
            return True
        return False


class Ticker:
    def __init__(self,
                 tick_interval_s: float):
        self.tick_interval = tick_interval_s
        self.counter: int = 0
        self.start_time = perf_counter()
        self.__block_flags = {}

    def update(self):
        prev = self.counter
        self.counter = int((perf_counter() - self.start_time) / self.tick_interval)
        for k in self.__block_flags:
            if self.counter % k != 0 and self.__block_flags[k]:
                self.__block_flags[k] = False
        return True if self.counter != prev else False

    def since(self, period_start: int) -> int:
        return self.counter - period_start

    def elapsed(self, period_len: int, period_start: int) -> bool:
        return True if self.since(period_start) >= period_len else False

    def mod(self,
            mod: int):
        if self.counter % mod == 0:
            return True
        return False

    def cmod(self,
             mod: int,
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
        if unblk and self.__block_flags[mod] and self.counter % mod != 0:
            self.__block_flags[mod] = False
        return False


class IncTicker:
    def __init__(self,
                 tick_interval_s: float):
        self.tick_interval = tick_interval_s
        self.counter: int = 0
        self.last_tick_time: float = perf_counter()
        self.__block_flags: dict[int, bool | None] = {}


    # should this catch up, or only increment once?
    def update(self):
        prev = self.counter
        now = perf_counter()
        elapsed_t = now - self.last_tick_time  # type: ignore
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now
        for k in self.__block_flags:
            if self.counter % k != 0 and self.__block_flags[k]:
                self.__block_flags[k] = False
        return True if self.counter != prev else False

    def mod(self,
            mod: int):
        if self.counter % mod == 0:
            return True
        return False

    def cmod(self,
             mod: int,
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
        if unblk and self.__block_flags[mod] and self.counter % mod != 0:
            self.__block_flags[mod] = False
        return False

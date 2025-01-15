from time import perf_counter

class Ticker:
    """
    Basic "ticker" timer, i.e. will increment a counter tracking a given period.
    """
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

    def since(self, period_start: int | None = None) -> int:
        period_start = period_start if period_start else 0  # 0 == start
        return self.counter - period_start

    def elapsed(self, period_len: int, period_start: int | None = None) -> bool:
        """
        Has a given period elapsed since period_start?
        """
        return True if self.since(period_start) >= period_len else False


class __TickerIntermediary(Ticker):
    """
    Private class to share functionality between child classes
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
        self.__block_flags = {}

    def cmod(self,
             mod: int,
             chk: bool = True,
             blk: bool = True,
             unblk: bool = True):
        # may implement a "cmod since" functionality
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


class ExtTicker(__TickerIntermediary):
    """
    Ticker with extended functionality - internally handled checks for a period having elapsed which avoid returning True more than once in a while loop.
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)

    def update(self):
        ticked = super().update()
        for k in self.__block_flags:
            if self.counter % k != 0 and self.__block_flags[k]:
                self.__block_flags[k] = False
        return ticked


class IncTicker(__TickerIntermediary):
    """
    Ticker with identical functionality to ExtTicker, excepting that when, upon calling update(), the tick interval has elapsed since the last call to update(), the ticker will *only* increment .counter by one, regardless of how much time has actually elapsed.
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
        self.last_tick_time: float = self.start_time

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


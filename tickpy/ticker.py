from time import perf_counter
from typing import Protocol


class __TickerParent():
    def __init__(self,
                 tick_interval_s: float):
        self.tick_interval: float = tick_interval_s
        self.counter: int = 0
        self.start_time: float = perf_counter()

    def mod(self,
            mod: int) -> bool:
        """
        Has a given period completed a cycle at the current value of .counter? mod as in 'modulo', i.e. .counter % mod
        """
        if self.counter % mod == 0:
            return True
        return False

    def since(self, period_start: int | None = None) -> int:
        """
        Ticks since period_start - if None, ticks since instance was created
        """
        period_start = period_start if period_start else 0  # 0 == start
        return self.counter - period_start

    def elapsed(self, period_len: int, period_start: int | None = None) -> bool:
        """
        Has a given period elapsed since period_start?
        """
        return True if self.since(period_start) >= period_len else False


class IncTicker(__TickerParent):
    """
    Basic "ticker" timer, i.e. will increment a counter tracking a given period.
    Each call to .udpate() will only ever increment the counter by 1.
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
        self.last_tick_time: float = self.start_time

    def update(self) -> bool:
        prev = self.counter
        now = perf_counter()
        elapsed_t = now - self.last_tick_time  # type: ignore
        if elapsed_t >= self.tick_interval:
            self.counter += 1
            self.last_tick_time = now
        # prev = self.counter
        # self.counter = int((perf_counter() - self.start_time) / self.tick_interval)
        return True if self.counter != prev else False


class FreeTicker(__TickerParent):
    """
    Basic "ticker" timer, i.e. will increment a counter tracking a given period.
    Each call to .udpate() will increment the counter by as many periods have passed since the last call to .update().
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
    

    def update(self) -> bool:
        prev = self.counter
        self.counter = int((perf_counter() - self.start_time) / self.tick_interval)
        return True if self.counter != prev else False


class __ExtProtocol(Protocol):
    tick_interval: float
    counter: int
    start_time: float
    _block_flags: dict[int, bool | None]

    def mod(self, mod: int) -> bool:
        ...


class __TickerMixin(__ExtProtocol):
    """
    Private class to share functionality between child classes
    """
    def _shared_init(self) -> None:
        """
        Private function to add to init of classes implementing .cmod()
        """
        self._block_flags = {}

    def cmod(self,
             mod: int) -> bool:
        """
        *C*omplex mod - check whether a given period x has elapsed given the current value of .counter, without returning True again if .cmod(x) is called more than once while counter remains at the same value.
        """
        period_elasped: bool = self.mod(mod)
        try:
            self._block_flags[mod]
        except KeyError:
            self._block_flags[mod] = False
        if period_elasped:
            if not self._block_flags[mod]:
                self._block_flags[mod] = True
                return True
        return False

    def _update_flags(self) -> None:
        """
        Private function to update blocking flags to be called each time the counter updates
        """
        for k in self._block_flags:
            if self.counter % k != 0 and self._block_flags[k]:
                self._block_flags[k] = False


class ExtFreeTicker(FreeTicker, __TickerMixin):
    """
    FreeTicker with extended functionality - see .cmod().
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
        self._shared_init()

    def update(self) -> bool:
        ticked = super().update()
        self._update_flags()
        return ticked


class ExtIncTicker(IncTicker, __TickerMixin):
    """
    Ticker with extended functionality - see .cmod().
    """
    def __init__(self,
                 tick_interval_s: float):
        super().__init__(tick_interval_s)
        self._shared_init()

    def update(self) -> bool:
        ticked = super().update()
        self._update_flags()
        return ticked

from time import perf_counter



class StaticTimer():
    """
    Timer that only updates its reference point when instructed, i.e. .now refers to the last time the timer was instructed to update
    """
    def __init__(self):
        self.start_time: float = perf_counter()
        self.now = self.start_time  # type: ignore

    def update(self):
        self.now = perf_counter()  # type: ignore

    def since(self, past_t: float | None = None) -> float:
        return self.now - (past_t if past_t else self.start_time)

    def elapsed(self, period_len: float, period_start: float | None = None) -> bool:
        return True if self.since((period_start if period_start else self.start_time))>= period_len else False


class Timer(StaticTimer):
    """
    Normal Timer, i.e. .now is always now
    """
    def __init__(self):
        self.start_time: float = perf_counter()

    @property
    def now(self) -> float:
        return perf_counter()

   

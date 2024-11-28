from time import perf_counter

class Timer:
    def __init__(self):
        self.start_time: float = perf_counter()

    @property
    def now(self) -> float:
        return perf_counter()

    def since(self, past_t: float | None = None) -> float:
        return self.now - (past_t if past_t else self.start_time)

    def elapsed(self, period_len: float, period_start: float | None = None) -> bool:
        return True if self.since((period_start if period_start else self.start_time))>= period_len else False

    

import heapq
from typing import Callable, Any
from dataclasses import dataclass, field
from tickpy.ticker import _TickerParent


# use partials if you want args set for call/post (for now)
@dataclass(order=True)
class Event:
    run_at: int
    call: Callable[..., None]
    post: Callable[..., None] | None = None


# if it becomes necessary, add key for ordering arguments with the same execution time (-1 if it doesn't matter)
class EventQueue:
    def __init__(self,
                 ticker_ref: _TickerParent):
        self.events: list[Event] = []
        self._ticker_ref = ticker_ref
    
    def schedule(self,
                 event: Event):
        breakpoint()
        heapq.heappush(self.events, event)
    
    def process_events(self):
        while self.events and self.events[0].run_at <= self._ticker_ref.counter:
            event = heapq.heappop(self.events)
            event.call()
            if event.post:
                event.post()

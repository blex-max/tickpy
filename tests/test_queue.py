from tickpy.ticker import IncTicker
from tickpy.queue import EventQueue, Event
import time


class DummyObj:
    def __init__(self):
        self.x = 0

    def inc(self):
        self.x += 1


def test_EventQueue():
    t = IncTicker(0.01)
    o = DummyObj()
    q = EventQueue(t)
    for i in range(1, 4):
        q.schedule(Event(
                       i,
                       o.inc,
                       o.inc
                   ))
    for i in [2, 4, 6]:
        time.sleep(0.011)
        t.update()
        q.process_events()
        assert o.x == i


# fish should pull tickpy from github commit for now

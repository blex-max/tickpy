from tickpy.timer import StaticTimer, Timer
import time

def test_StaticTimers():
    t = StaticTimer()
    time.sleep(0.02)
    t.update()
    assert (lambda x: int(x * 10**2) / 10**2)(t.since()) == 0.02
    assert t.elapsed(0.02) == True

def test_timers():
    t = Timer()
    time.sleep(0.02)
    assert (lambda x: int(x * 10**2) / 10**2)(t.since()) == 0.02
    assert t.elapsed(0.02) == True

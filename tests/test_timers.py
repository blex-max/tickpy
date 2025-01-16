from tickpy.timer import StaticTimer
import time

def test_timers():
    t = StaticTimer()
    time.sleep(0.02)
    t.update()
    assert (lambda x: int(x * 10**2) / 10**2)(t.since()) == 0.02
    assert t.elapsed(0.02) == True

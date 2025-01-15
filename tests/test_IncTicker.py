from tickpy.ticker import IncTicker
import time


def test_IncTicker():
    t = IncTicker(0.02)
    assert t.counter == 0
    time.sleep(0.02)
    t.update()
    assert t.counter == 1
    time.sleep(0.02)
    t.update()
    assert t.counter == 2
    assert t.cmod(2) == True
    assert t.cmod(2) == False
    time.sleep(0.02)
    t.update()
    assert t.counter == 3
    assert t.cmod(2) == False
    time.sleep(0.02)
    t.update()
    assert t.counter == 4
    assert t.cmod(2) == True
    assert t.cmod(2) == False
    assert t.cmod(4) == True
    assert t.cmod(4) == False
    time.sleep(0.02)
    t.update()
    time.sleep(0.02)
    t.update()
    time.sleep(0.02)
    t.update()
    time.sleep(0.02)
    t.update()
    assert t.counter == 8
    assert t.cmod(2) == True
    assert t.cmod(2) == False
    assert t.cmod(4) == True
    assert t.cmod(4) == False



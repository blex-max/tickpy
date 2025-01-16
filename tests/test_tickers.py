from tickpy.ticker import ExtTicker, ExtFreeTicker
import time


def test_ExtTicker_basic():
    t = ExtTicker(0.02)
    assert t.counter == 0
    time.sleep(0.01)
    assert t.update() == False
    assert t.counter == 0
    time.sleep(0.01)
    assert t.update() == True
    assert t.counter == 1


def test_ExtFreeTicker_basic():
    t = ExtFreeTicker(0.02)
    assert t.counter == 0
    time.sleep(0.01)
    assert t.update() == False
    time.sleep(0.01)
    assert t.update() == True
    assert t.counter == 1


def test_period_funcs():
    t = ExtFreeTicker(0.02)
    time.sleep(0.05)
    t.update()
    assert t.mod(2) == True
    time.sleep(0.05)
    t.update()
    assert t.since() == 5
    assert t.since(2) == 3
    assert t.elapsed(4) == True
    assert t.elapsed(6) == False
    assert t.elapsed(2, 2) == True
    assert t.elapsed(8, 2) == False
    assert t.mod(2) == False
    assert t.mod(5) == True


def test_cmod():
    t = ExtFreeTicker(0.02)
    time.sleep(0.04)
    t.update()
    assert t.cmod(2) == True
    assert t.cmod(2) == False
    time.sleep(0.02)
    t.update()
    assert t.cmod(2) == False
    time.sleep(0.02)
    t.update()
    assert t.cmod(2) == True
    assert t.cmod(2) == False

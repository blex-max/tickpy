from pytick.ticker import MinTicker
import time


def test_MinTicker():
    t = MinTicker(0.2)
    assert t.counter == 0
    time.sleep(0.5)
    t.update()
    assert t.counter == 2
    assert t.mod(2) == True
    time.sleep(0.5)
    t.update()
    assert t.counter == 5
    assert t.mod(2) == False
    assert t.mod(5) == True

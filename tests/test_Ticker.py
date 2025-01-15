from tickpy.ticker import Ticker
import time


def test_Ticker():
    t = Ticker(0.2)
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
    assert t.since() == 5
    assert t.since(2) == 3
    assert t.elapsed(4) == True
    assert t.elapsed(6) == False
    assert t.elapsed(2, 2) == True
    assert t.elapsed(8, 2) == False

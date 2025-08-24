
import importlib

def test_q3():
    q3 = importlib.import_module("q3")
    assert abs(q3.circle_area(7) - 153.86) < 0.01

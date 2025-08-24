
import importlib

def test_q2():
    q2 = importlib.import_module("q2")
    assert q2.rectangle_description(10, 5) == "The rectangle has length 10 and width 5"

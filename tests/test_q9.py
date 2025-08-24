
import importlib

def test_q9():
    q9 = importlib.import_module("q9")
    assert q9.rectangle_perimeter(10, 4) == 28

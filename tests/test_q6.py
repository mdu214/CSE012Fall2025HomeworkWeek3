
import importlib

def test_q6():
    q6 = importlib.import_module("q6")
    assert q6.longest_side(5, 12, 9) == "b"

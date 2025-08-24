
import importlib

def test_q5():
    q5 = importlib.import_module("q5")
    assert q5.square_or_rectangle(5, 5) == "This is a square!"
    assert q5.square_or_rectangle(10, 5) == "This is a rectangle."

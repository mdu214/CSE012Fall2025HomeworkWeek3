
import importlib

def test_q4():
    q4 = importlib.import_module("q4")
    types = q4.variable_types(10, 3.14*7*7)
    assert types == (int, float)

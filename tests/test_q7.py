
import importlib

def test_q7():
    q7 = importlib.import_module("q7")
    assert q7.uppercase_shapes(["circle", "square"]) == ["CIRCLE", "SQUARE"]

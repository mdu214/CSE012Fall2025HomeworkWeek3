
import importlib

def test_q8():
    q8 = importlib.import_module("q8")
    assert q8.triangle_count(3) == [
        "This is triangle number 1",
        "This is triangle number 2",
        "This is triangle number 3",
    ]

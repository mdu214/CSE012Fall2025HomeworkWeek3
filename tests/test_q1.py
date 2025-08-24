
import importlib

def test_q1():
    q1 = importlib.import_module("q1")
    assert q1.format_shape_name("  rectangle  ") == "RECTANGLE"

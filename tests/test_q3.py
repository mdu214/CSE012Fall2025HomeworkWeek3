# tests/test_q3.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q3_square():
    mod = importlib.import_module("q3")
    assert mod.square(4) == 16
    assert mod.square(-3) == 9

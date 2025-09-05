# tests/test_q2.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q2_add():
    mod = importlib.import_module("q2")
    assert mod.add(2, 3) == 5
    assert mod.add(-1, 1) == 0

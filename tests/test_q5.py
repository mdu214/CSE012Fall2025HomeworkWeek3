# tests/test_q5.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q5_sum_all():
    mod = importlib.import_module("q5")
    assert mod.sum_all(1, 2, 3) == 6
    assert mod.sum_all() == 0
    assert mod.sum_all(10, -5, 5) == 10

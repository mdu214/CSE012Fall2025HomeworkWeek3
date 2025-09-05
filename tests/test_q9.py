# tests/test_q9.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q9_square_lambda():
    mod = importlib.import_module("q9")
    assert mod.square_lambda(5) == 25
    assert mod.square_lambda(-2) == 4

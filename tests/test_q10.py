# tests/test_q10.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q10_shout_nested():
    mod = importlib.import_module("q10")
    assert mod.shout("hello") == "HELLO"
    assert mod.shout("Python") == "PYTHON"

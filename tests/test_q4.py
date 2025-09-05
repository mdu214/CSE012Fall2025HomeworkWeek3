# tests/test_q4.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q4_greet_default():
    mod = importlib.import_module("q4")
    assert mod.greet_default() == "Hello, World!"
    assert mod.greet_default("Bob") == "Hello, Bob!"

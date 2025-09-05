# tests/test_q7.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q7_local_shadow():
    mod = importlib.import_module("q7")
    assert mod.local_shadow(999) == 5

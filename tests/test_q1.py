# tests/test_q1.py
import importlib, pathlib
sys_path = str(pathlib.Path(__file__).resolve().parents[1])
import sys; sys.path.append(sys_path)

def test_q1_greet():
    mod = importlib.import_module("q1")
    assert mod.greet("Alice") == "Hello, Alice!"

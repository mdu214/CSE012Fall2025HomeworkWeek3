# tests/test_q8.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q8_multiply_docstring():
    mod = importlib.import_module("q8")
    assert mod.multiply(2, 4) == 8
    doc = mod.multiply.__doc__
    assert doc is not None and "parameters" in doc.lower()

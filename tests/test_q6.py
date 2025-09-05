# tests/test_q6.py
import importlib, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

def test_q6_print_info():
    mod = importlib.import_module("q6")
    result = mod.print_info(name="Alice", age=30)
    assert isinstance(result, dict)
    assert result["name"] == "Alice"
    assert result["age"] == 30


import importlib

def test_q10():
    q10 = importlib.import_module("q10")
    shapes = ["circle", "square", "triangle", "rectangle"]
    inputs = ["circle", "hexagon", "quit", "triangle"]
    results = q10.choose_shape(inputs, shapes)
    assert results == ["You chose a valid shape!", "Unknown shape."]

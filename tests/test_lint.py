
import subprocess

def test_pylint_conformance():
    '''Run pylint on all q#.py files (q1.py ... q10.py)'''
    for i in range(1, 11):
        filename = f"q{i}.py"
        result = subprocess.run(
            ["pylint", "--disable=R,C", filename],
            capture_output=True, text=True
        )
        print(result.stdout)
        if "rated at" in result.stdout:
            score_str = result.stdout.split("rated at")[-1].split("/")[0].strip()
            try:
                score = float(score_str)
                assert score >= 7.0, f"Pylint score too low in {filename}: {score}"
            except ValueError:
                assert False, f"Could not parse pylint score for {filename}"
        else:
            assert False, f"No pylint rating found for {filename}"

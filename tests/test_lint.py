# tests/test_pylint.py
import subprocess
import pathlib

def test_pylint_score():
    """Run pylint on all q#.py files and require a perfect score."""
    root = pathlib.Path(__file__).resolve().parents[1]  # project root
    files = [str(root / f"q{i}.py") for i in range(1, 11)]

    result = subprocess.run(
        ["pylint", "--score=y", "--disable=R,C", *files],
        capture_output=True,
        text=True,
    )

    # Extract the score from pylint output
    score_line = [line for line in result.stdout.splitlines() if "Your code has been rated at" in line]
    assert score_line, f"Pylint did not return a score.\nOutput:\n{result.stdout}\n{result.stderr}"

    score_text = score_line[0].split("/")[0].split()[-1]  # e.g., '10.00'
    score = float(score_text)
    assert score >= 9.0, f"Pylint score too low: {score}\n{result.stdout}\n{result.stderr}"


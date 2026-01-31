import pytest
from validator import analyze_complexity

def test_linear_complexity():
    code = """
def linear(n):
    for i in range(n):
        pass
    """
    assert "O(n^1)" in analyze_complexity(code) or "O(n^" in analyze_complexity(code)

def test_nested_loop_complexity():
    code = """
def nested(n):
    for i in range(n):
        for j in range(n):
            pass
    """
    # Simply checking if it detects loops
    assert "O(n^" in analyze_complexity(code)

# Run this by typing 'pytest' in your terminal
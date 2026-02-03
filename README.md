# Polyglot Logic Validator

**Polyglot Logic Validator** is a powerful Python tool designed to analyze the algorithmic complexity of your code. It combines static analysis (AST parsing) with dynamic analysis (runtime metrics) to provide a comprehensive view of your algorithm's performance.

![Complexity Proof Graph](complexity_proof.png)

## 🚀 Features

-   **Static Code Analysis**: detection of loop structures to estimate Big-O complexity (e.g., O(1), O(n), O(n^2)).
-   **Dynamic Performance Metrics**: Measures actual execution time and memory usage.
-   **Visual Complexity Proof**: Generates `complexity_proof.png`, a graph comparing your code's runtime against standard complexity curves (like O(n^2)).
-   **Correctness Verification**: Safely executes code in a sandbox environment to verify outputs against expected results.

## 🛠️ Installation

Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install matplotlib psutil
```

For running tests:
```bash
pip install pytest
```

## 📖 Usage

### 1. Analyzing Complexity & Performance

You can analyze a function's complexity and measure its runtime using existing modules.

```python
from validator import analyze_complexity, measure_runtime, generate_complexity_graph

def sample_algo(n):
    return [i*j for i in range(n) for j in range(n)]

# Static Analysis
code_str = """
def sample_algo(n):
    return [i*j for i in range(n) for j in range(n)]
"""
print(f"Estimated Complexity: {analyze_complexity(code_str)}")

# Dynamic Measurement
metrics = measure_runtime(sample_algo, 100)
print(f"Runtime: {metrics['time']}, Memory: {metrics['memory']}")

# Generate Visual Graph
generate_complexity_graph(sample_algo)
```

### 2. Running Tests

To verify the validator itself, run the included tests:

```bash
pytest test_validator.py
```

## 📂 Project Structure

-   `validator.py`: Core logic for analysis, metrics, and graph generation.
-   `test_validator.py`: Unit tests ensuring the analyzer detects loops correctly.
-   `complexity_proof.png`: Generated output showing performance visualization.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is open-source.

# Python exercises

[![Python CI](https://github.com/PADOALEX/Home-Work-by-PADO-Python/actions/workflows/ci.yml/badge.svg)](https://github.com/PADOALEX/Home-Work-by-PADO-Python/actions/workflows/ci.yml)

An academic generalized Fibonacci exercise by Oleksandr Durmanenko. The original submission remains on [Task_1_Fibonacci_Durmanenko](https://github.com/PADOALEX/Home-Work-by-PADO-Python/tree/Task_1_Fibonacci_Durmanenko); the maintained version is now discoverable on the default branch.

## Run and test

Requires Python 3.12+ and no third-party packages:

```bash
python Fibonacci_Durmanenko/Fibonacci.py
python -m unittest discover -s tests -v
```

Edit the three sample input files beside the script, or pass `--input-dir /path/to/inputs`. Each seed and range endpoint occupies one line. Output is written to `output.txt` in that directory after all inputs and calculations succeed. Importing the module performs no file operations.

## Behavior

- `fibonacci(steps, array)` appends exactly `steps` values to the supplied list using iteration. Integer inputs retain arbitrary-precision integer arithmetic.
- `fibonaccirange(start, end, array)` extends the supplied sequence until its last value reaches the upper endpoint and returns values in the inclusive interval.
- Seeds must be finite and nonnegative. Negative steps, inverted ranges, two zero seeds unable to reach a positive endpoint, and floating-point overflow raise explicit errors.
- Unit tests cover sequences, 2,000 steps, range boundaries, invalid inputs, overflow and CLI file paths.

This is a mathematical learning exercise, without a web service, database or authentication.

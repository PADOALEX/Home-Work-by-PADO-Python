import argparse
import math
from pathlib import Path


def _validate_seed(array):
    if len(array) < 2:
        raise ValueError("At least two seed values are required")
    if any(not isinstance(value, (int, float)) or value < 0 or
           isinstance(value, float) and not math.isfinite(value) for value in array):
        raise ValueError("Seed values must be finite, nonnegative numbers")


def _append_next(array):
    value = array[-1] + array[-2]
    if isinstance(value, float) and not math.isfinite(value):
        raise ArithmeticError("Fibonacci value exceeds floating-point range")
    array.append(value)


def fibonacci(steps, array):
    if not isinstance(steps, int) or steps < 0:
        raise ValueError("Steps must be a nonnegative integer")
    _validate_seed(array)
    for _ in range(steps):
        _append_next(array)
    return array


def fibonaccirange(start, end, array):
    _validate_seed(array)
    if not all(isinstance(value, (int, float)) and
               (not isinstance(value, float) or math.isfinite(value)) for value in (start, end)):
        raise ValueError("Range endpoints must be finite numbers")
    if start > end:
        raise ValueError("Range start must not exceed range end")
    if array[-1] == 0 and array[-2] == 0 and end > 0:
        raise ValueError("Two zero seeds cannot reach a positive range endpoint")
    while array[-1] < end:
        _append_next(array)
    return [value for value in array if start <= value <= end]


def _number(text):
    try:
        return int(text)
    except ValueError:
        value = float(text)
        if not math.isfinite(value):
            raise ValueError("Input numbers must be finite")
        return value


def main():
    parser = argparse.ArgumentParser(description="Generate a generalized Fibonacci sequence")
    parser.add_argument("--input-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    directory = args.input_dir
    seed = [_number(line) for line in (directory / "input_2_numbers.txt").read_text().splitlines()]
    if len(seed) != 2:
        raise ValueError("input_2_numbers.txt must contain exactly two numbers")
    steps = int((directory / "fibonacci_steps.txt").read_text().strip())
    endpoints = [_number(line) for line in (directory / "range_start_end.txt").read_text().splitlines()]
    if len(endpoints) != 2:
        raise ValueError("range_start_end.txt must contain exactly two endpoints")
    sequence = fibonacci(steps, seed.copy())
    selected = fibonaccirange(*endpoints, seed.copy())
    output = f"Algorithm Fibonacci with {steps} steps:\n" + " ".join(map(str, sequence))
    output += f"\nAlgorithm Fibonacci in range from {endpoints[0]} to {endpoints[1]}:\n"
    output += " ".join(map(str, selected))
    (directory / "output.txt").write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()

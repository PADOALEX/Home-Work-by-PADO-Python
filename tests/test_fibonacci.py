import importlib.util
import pathlib
import subprocess
import sys
import tempfile
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "Fibonacci_Durmanenko/Fibonacci.py"
spec = importlib.util.spec_from_file_location("fibonacci_exercise", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FibonacciTests(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], module.fibonacci(5, [0, 1]))

    def test_large_step_count_is_iterative(self):
        self.assertEqual(2002, len(module.fibonacci(2000, [0, 1])))

    def test_zero_steps(self):
        self.assertEqual([2, 3], module.fibonacci(0, [2, 3]))

    def test_invalid_steps(self):
        for steps in (-1, 1.5):
            with self.subTest(steps=steps), self.assertRaises(ValueError):
                module.fibonacci(steps, [0, 1])

    def test_invalid_seeds(self):
        for seed in ([], [1], [-1, 1], [float("nan"), 1], [0, float("inf")]):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                module.fibonacci(2, seed)

    def test_inclusive_range(self):
        self.assertEqual([5, 8, 13], module.fibonaccirange(5, 13, [0, 1]))

    def test_empty_range(self):
        self.assertEqual([], module.fibonaccirange(6, 7, [0, 1]))

    def test_bad_ranges(self):
        for start, end in ((10, 1), (0, float("nan")), (0, float("inf"))):
            with self.subTest(start=start, end=end), self.assertRaises(ValueError):
                module.fibonaccirange(start, end, [0, 1])

    def test_zero_seed_does_not_loop_forever(self):
        with self.assertRaises(ValueError):
            module.fibonaccirange(0, 10, [0, 0])

    def test_float_overflow(self):
        with self.assertRaises(ArithmeticError):
            module.fibonacci(1, [1e308, 1e308])

    def test_files_resolve_outside_working_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            directory = pathlib.Path(folder)
            (directory / "input_2_numbers.txt").write_text("0\n1\n")
            (directory / "fibonacci_steps.txt").write_text("5\n")
            (directory / "range_start_end.txt").write_text("5\n13\n")
            subprocess.run([sys.executable, str(SOURCE), "--input-dir", folder], cwd=folder, check=True)
            self.assertIn("0 1 1 2 3 5 8", (directory / "output.txt").read_text())
            self.assertIn("5 8 13", (directory / "output.txt").read_text())


if __name__ == "__main__":
    unittest.main()

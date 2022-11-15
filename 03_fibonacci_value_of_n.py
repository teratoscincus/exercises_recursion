import unittest


def fibonacci_value(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_value(n - 1) + fibonacci_value(n - 2)


class FibonacciValueTestCase(unittest.TestCase):
    def test_n_0(self):
        self.assertEqual(fibonacci_value(0), 0)

    def test_n_1(self):
        self.assertEqual(fibonacci_value(1), 1)

    def test_n_2(self):
        self.assertEqual(fibonacci_value(2), 1)

    def test_n_5(self):
        self.assertEqual(fibonacci_value(5), 5)

    def test_n_6(self):
        self.assertEqual(fibonacci_value(6), 8)


if __name__ == "__main__":
    unittest.main()

import unittest
from fibonacci import fibonacci, memo

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_negative_input(self):
        with self.assertRaises(ValueError) as cm:
            fibonacci(-1)
        self.assertEqual(str(cm.exception), 'Input must be a non-negative integer')

    def test_non_integer_input(self):
        with self.assertRaises(ValueError) as cm:
            fibonacci('a')
        self.assertEqual(str(cm.exception), 'Input must be a non-negative integer')

    def test_large_input(self):
        self.assertEqual(fibonacci(50), 12586269025)
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_memoization(self):
        self.assertEqual(fibonacci(100), fibonacci(100))
        self.assertIn(100, memo)

if __name__ == '__main__':
    unittest.main()

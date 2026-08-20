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

    def test_memoization_performance(self):
        import time
        start_time = time.time()
        fibonacci(100)
        end_time = time.time()
        self.assertLess(end_time - start_time, 0.1)

    def test_memoization_optimization(self):
        self.assertEqual(fibonacci(100), fibonacci(100))
        self.assertIn(100, memo)
        self.assertEqual(len(memo), 101)

    def test_memoization_optimization_large_input(self):
        import time
        start_time = time.time()
        fibonacci(1000)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1)

    def test_memoization_optimization_clear_cache(self):
        fibonacci(1000)
        self.assertIn(1000, memo)
        fibonacci(0)
        self.assertNotIn(1000, memo)

    def test_memoization_optimization_clear_cache_large_input(self):
        fibonacci(1000)
        self.assertIn(1000, memo)
        fibonacci(0)
        self.assertNotIn(1000, memo)
        self.assertEqual(len(memo), 2)

if __name__ == '__main__':
    unittest.main()

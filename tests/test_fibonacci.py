import unittest
from fibonacci import fibonacci

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
        with self.assertRaises(SystemExit) as cm:
            fibonacci(-1)
        self.assertEqual(cm.exception.code, 1)

    def test_non_integer_input(self):
        with self.assertRaises(SystemExit) as cm:
            fibonacci('a')
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
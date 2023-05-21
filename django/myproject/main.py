import unittest

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

class TestFunctions(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_evenness(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

if __name__ == '__main__':
    unittest.main()

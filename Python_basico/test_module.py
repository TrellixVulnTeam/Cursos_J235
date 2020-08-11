import unittest

def multiplication(x, a):
    return x * a

class TestString(unittest.TestCase):

    def test_multiplication(self):
        y = multiplication(1, 3)
        self.assertEqual(y, 3)

    def test_sum(self):
        y = 4 + 4
        self.assertEqual(y, 8)


if __name__ == '__main__':
    unittest.main()

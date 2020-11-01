import unittest

from utils.PermutUtils import d_min_swap


class TestCase(unittest.TestCase):
    def test_d_min_swap(self):
        arr = [1, 5, 4, 3, 2]
        self.assertEqual(d_min_swap(arr), 2)
        arr = [8, 9, 16, 15]
        self.assertEqual(d_min_swap(arr), 1)


if __name__ == '__main__':
    unittest.main()

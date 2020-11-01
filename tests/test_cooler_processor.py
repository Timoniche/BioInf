import unittest

from cool.CoolerProcessor import expected_avg_on_k, dispersion_avg_on_k


class TestCase(unittest.TestCase):
    def test_expected(self):
        test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        e_k0 = expected_avg_on_k(test_matrix, 0)
        e_k1 = expected_avg_on_k(test_matrix, 1)
        e_k2 = expected_avg_on_k(test_matrix, 2)
        ans_k0 = (1 + 5 + 9) / 3
        ans_k1 = (4 + 8 + 2 + 6) / 4
        ans_k2 = (7 + 3) / 2
        self.assertEqual(e_k0, ans_k0)
        self.assertEqual(e_k1, ans_k1)
        self.assertEqual(e_k2, ans_k2)

    def test_dispersion(self):
        test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        d_k0 = dispersion_avg_on_k(test_matrix, 0)
        d_k1 = dispersion_avg_on_k(test_matrix, 1)
        d_k2 = dispersion_avg_on_k(test_matrix, 2)

        e_k0 = (1 + 5 + 9) / 3
        e_k1 = (4 + 8 + 2 + 6) / 4
        e_k2 = (7 + 3) / 2

        e2_k0 = (1 * 1 + 5 * 5 + 9 * 9) / 3
        e2_k1 = (4 * 4 + 8 * 8 + 2 * 2 + 6 * 6) / 4
        e2_k2 = (7 * 7 + 3 * 3) / 2

        ans_k0 = e2_k0 - e_k0 ** 2
        ans_k1 = e2_k1 - e_k1 ** 2
        ans_k2 = e2_k2 - e_k2 ** 2

        # todo: how lib compares floats...? (which eps)
        self.assertEqual(d_k0, ans_k0)
        self.assertEqual(d_k1, ans_k1)
        self.assertEqual(d_k2, ans_k2)


"""
1 2 3
4 5 6
7 8 9
"""
if __name__ == '__main__':
    # k0_arr = [1, 5, 9]
    # k1_arr = [4, 8, 2, 6]
    # k2_arr = [7, 3]
    unittest.main()

from math import sqrt

import logging
import cooler

"""
k := 1
00000
*0000
0*000
00*00
000*0
"""


def get_bottom_k_diagonal(mat, k):
    n = len(mat)
    ret = []
    i = k
    for j in range(0, n - k):
        ret.append(mat[i][j])
        i += 1
        j += 1
    return ret


"""
k := 1
0*000
00*00
000*0
0000*
00000
"""


def get_upper_k_diagonal(mat, k):
    n = len(mat)
    ret = []
    i = 0
    for j in range(k, n):
        ret.append(mat[i][j])
        i += 1
        j += 1
    return ret


"""
Pre: list1.size() == list2.size()
"""


def count_ev(bottom, upper):
    cnt = len(bottom)
    return (sum(bottom) + sum(upper)) / (2 * cnt)


def expected_avg_on_k(mat, k):
    bottom = get_bottom_k_diagonal(mat, k)
    upper = get_upper_k_diagonal(mat, k)
    return count_ev(bottom, upper)


def dispersion_avg_on_k(mat, k):
    bottom = get_bottom_k_diagonal(mat, k)
    upper = get_upper_k_diagonal(mat, k)
    bottom2 = [*map(lambda x: x ** 2, bottom)]
    upper2 = [*map(lambda x: x ** 2, upper)]
    ev2 = count_ev(bottom2, upper2)
    ev = count_ev(bottom, upper)
    dispersion = ev2 - (ev ** 2)
    return dispersion


"""
Pre: k < len(matrix)
"""


def process_cool(filepath, k=10):
    logging.basicConfig(filename="logs/cooler.log", level=logging.INFO)
    c = cooler.Cooler(filepath)
    mat = c.matrix(balance=False)[:, :]
    assert len(mat) > k > 0, "k should be in ( 0 ; len(matrix) )"
    expec = expected_avg_on_k(mat, k)
    disp = dispersion_avg_on_k(mat, k)
    sigma = sqrt(disp)
    logging.info('k is r(i, j): such points as (i, i + k), (i, i - k)')
    logging.info(f'k := {k}')
    logging.info(f'EX = {expec}')
    logging.info(f'DX = {disp}')
    logging.info(f'SIGMA = {sigma}')
    logging.info('3-sigma rule:')
    logging.info('with >= 8/9 probability (i,j) blocks have')
    logging.info(f'[{max(0, expec - 3 * sigma)}; {expec + 3 * sigma}] connections')
    return sigma

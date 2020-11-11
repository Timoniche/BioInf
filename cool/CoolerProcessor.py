import math
from math import sqrt
from matplotlib import pyplot as plt

import logging

import cooler
from numpy import np


def check_symmetry(mtx):
    n = len(mtx)
    for i in range(n):
        for j in range(n):
            if mtx[i][j] != mtx[j][i]:
                return False
    return True


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


def count_ev(arr):
    cnt = len(arr)
    return sum(arr) / cnt


"""
Pre: mat is symmetrical
"""


def expected_avg_on_k(mat, k):
    upper = get_upper_k_diagonal(mat, k)
    return count_ev(upper)


"""
Pre: mat is symmetrical
"""


def dispersion_avg_on_k(mat, k):
    upper = get_upper_k_diagonal(mat, k)
    upper2 = [*map(lambda x: x ** 2, upper)]
    ev2 = count_ev(upper2)
    ev = count_ev(upper)
    dispersion = ev2 - (ev ** 2)
    return dispersion


def histogram(filepath, k=11):
    c = cooler.Cooler(filepath)
    bin_size = 500000
    count_bins_chr1 = math.ceil(c.chromsizes[0] / bin_size)
    contact_matrix = c.matrix(balance=False)[:count_bins_chr1, :count_bins_chr1]
    diag = get_upper_k_diagonal(contact_matrix, k)
    hist = np.histogram(np.array(diag))
    plt.hist(hist)

"""
Pre: k < len(matrix)
"""


def process_cool(contact_matrix, k=10):
    logging.info(f'symmetry: {check_symmetry(contact_matrix)}')
    # assert len(contact_matrix) > k > 0, "k should be in ( 0 ; len(matrix) )"
    assert len(contact_matrix) > k, "k should be in [ 0 ; len(matrix) )" # so far for task 3

    expec = expected_avg_on_k(contact_matrix, k)
    disp = dispersion_avg_on_k(contact_matrix, k)
    sigma = sqrt(disp)

    logging.info('k is r(i, j): such points as (i, i + k), (i, i - k)')
    logging.info(f'k := {k}')
    logging.info(f'EX = {expec}')
    logging.info(f'DX = {disp}')
    logging.info(f'SIGMA = {sigma}')
    logging.info('3-sigma rule:')
    logging.info('with >= 8/9 probability (i,j) blocks have')
    logging.info(f'[{max(0, expec - 3 * sigma)}; {expec + 3 * sigma}] connections')

    return expec, disp, sigma

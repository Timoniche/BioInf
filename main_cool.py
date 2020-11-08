import math

import cooler
import logging

from cool.CoolerProcessor import process_cool

import matplotlib.pyplot as plt


# def build_plot(contact_matrix):
#     # max = 6207
#     ex_disp_sigma = []
#     rng_k = range(10, 12)
#     ks = [k for k in rng_k]
#     for k in rng_k:
#         ex_disp_sigma.append(process_cool(contact_matrix, k))
#     plt.title('EX, DX, sigma(k)')
#     plt.xlabel('k')
#     plt.ylabel('value')
#     plt.plot(ks, [row[0] for row in ex_disp_sigma], color='red')
#     plt.plot(ks, [row[1] for row in ex_disp_sigma], color='green')
#     plt.plot(ks, [row[2] for row in ex_disp_sigma], color='blue')
#     plt.show()


def theory():
    logging.basicConfig(filename='logs/theory.log', filemode='w', level=logging.INFO)
    c = cooler.Cooler(filepath)
    step_bin = 500000
    count_bins_chr1 = math.ceil(c.chromsizes[0] / step_bin)
    # logging.info(c.chromsizes)
    # logging.info(c.chroms()[:])
    # logging.info(c.bins()[:])
    print(c.bins()[:count_bins_chr1])
    contact_matrix = c.matrix(balance=False)[:count_bins_chr1, :count_bins_chr1]
    logging.info(f'contact matrix:\n{contact_matrix}')

    # range_k = range(1, count_bins_chr1)
    range_k = range(11, 25)

    ks = [k for k in range_k]
    ex_disp_sigma = []
    for k in range_k:
        ex_disp_sigma.append(process_cool(contact_matrix, k))
    plt.title('chr 1: SIGMA(k)')
    plt.xlabel('k')
    plt.ylabel('SIGMA')
    plt.plot(ks, [row[0] for row in ex_disp_sigma], color='red')
    # plt.plot(ks, [row[1] for row in ex_disp_sigma], color='green')
    # plt.plot(ks, [row[2] for row in ex_disp_sigma], color='blue')
    plt.show()


def main():
    theory()


if __name__ == '__main__':
    filepath = 'data/Rao2014-IMR90-MboI-allreps-filtered.500kb.cool'
    main()

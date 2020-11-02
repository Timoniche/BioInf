from random import sample

import logging

import matplotlib.pyplot as plt

from utils.PermutUtils import d_min_swap, permut_cycles


def swap2(data):
    n = len(data)
    pair = sample(range(n), 2)
    data[pair[0]], data[pair[1]] = data[pair[1]], data[pair[0]]


def main():
    logging.basicConfig(filename="logs/permut.log", level=logging.INFO)
    n = 1000
    iterations = n
    data = [i for i in range(1, n + 1)]
    xs = [i for i in range(1, iterations + 1)]
    plt.title('real/random swaps')
    plt.xlabel('swap number')
    plt.ylabel('distance')
    plt.plot(xs, xs)
    real_dists = []
    delta_dists = []
    cnt_cycles = []
    for i in range(iterations):
        swap2(data)
        d = d_min_swap(data)
        real_dists.append(d)
        cnt = permut_cycles(data)
        cnt_cycles.append(cnt)
        logging.info(f'step: {i + 1}, cnt: {cnt}')
        delta_dists.append(i + 1 - d)
    plt.plot(xs, real_dists, color='red')
    # plt.plot(xs, delta_dists, color='green')
    # plt.plot(xs, cnt_cycles, color='black')
    plt.show()


if __name__ == '__main__':
    main()

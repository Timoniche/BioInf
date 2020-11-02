from random import sample

import matplotlib.pyplot as plt

from utils.PermutUtils import d_min_swap


def swap2(data):
    n = len(data)
    pair = sample(range(n), 2)
    data[pair[0]], data[pair[1]] = data[pair[1]], data[pair[0]]


def main():
    n = 100
    iterations = 5 * n
    data = [i for i in range(1, n + 1)]
    xs = [i for i in range(1, iterations + 1)]
    plt.title('real/random swaps')
    plt.xlabel('swap number')
    plt.ylabel('distance')
    plt.plot(xs, xs)
    real_dists = []
    for i in range(iterations):
        swap2(data)
        real_dists.append(d_min_swap(data))
    plt.plot(xs, real_dists, color='red')
    plt.show()


if __name__ == '__main__':
    main()

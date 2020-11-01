from random import sample

import matplotlib.pyplot as plt

from utils.PermutUtils import d_min_swap


def break2(data):
    n = len(data)
    pair = sample(range(n), 2)
    data[pair[0]], data[pair[1]] = data[pair[1]], data[pair[0]]


def main():
    n = 100
    data = [i for i in range(1, n + 1)]
    # print(data)
    xs = [i for i in range(1, n + 1)]
    plt.title('real/random swaps')
    plt.xlabel('swap number')
    plt.ylabel('distance')
    plt.plot(xs, xs)
    real_dists = []
    for i in range(n):
        break2(data)
        # print(data)
        real_dists.append(d_min_swap(data))
    plt.plot(xs, real_dists, color='red')
    plt.show()


if __name__ == '__main__':
    main()

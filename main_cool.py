from cool.CoolerProcessor import process_cool

import matplotlib.pyplot as plt


def main():
    # max = 6207
    sigmas = []
    rng_k = range(10, 12)
    ks = [k for k in rng_k]
    for k in rng_k:
        sigmas.append(process_cool(filepath, k))
    plt.title('sigma(k)')
    plt.xlabel('k')
    plt.ylabel('sigma')
    plt.plot(ks, sigmas, color='blue')
    plt.show()


if __name__ == '__main__':
    filepath = 'data/Rao2014-IMR90-MboI-allreps-filtered.500kb.cool'
    main()

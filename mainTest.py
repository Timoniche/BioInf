import math

import cooler


def get_matrix(filepath='data/Rao2014-IMR90-MboI-allreps-filtered.500kb.cool'):
    c = cooler.Cooler(filepath)
    bin_size = 500000
    print(c.info)
    count_bins_chr1 = math.ceil(c.chromsizes[0] / bin_size)
    return c.matrix(balance=False)[:count_bins_chr1, :count_bins_chr1]


def main():
    print('hi!')
    hic_file = open('hics/FIRST.txt', 'w')
    hic_full = get_matrix()
    dim = len(hic_full)
    for i in range(dim):
        for j in range(i, dim):
            hic_file.write(f'{i + 1} {j + 1} {hic_full[i][j]}\n')
    hic_file.close()


if __name__ == '__main__':
    main()
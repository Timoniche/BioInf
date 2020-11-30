import math
import numpy as np

import mdtraj as md
import matplotlib.pyplot as plt

_bins_cnt = 1000


def dist3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def curve_dist_matrix(arr):
    contact_matrix = np.array([[0.0 for _ in range(_bins_cnt)] for _ in range(_bins_cnt)])
    for i in range(_bins_cnt):
        for j in range(i + 1, _bins_cnt):  # from i + 1 as i is already == 0
            fst = arr[i]
            snd = arr[j]
            contact_matrix[i][j] = contact_matrix[j][i] = dist3d(fst[0], fst[1], fst[2], snd[0], snd[1], snd[2])
    return contact_matrix


pdbfile = 'plotted_hics/hic_full_1605996591721.pdb'
traj = md.load_pdb(pdbfile)
mat = traj.xyz[0]
dist_mat = curve_dist_matrix(mat)
print(mat)
print(dist_mat)
plt.title('dist from 3d curve')
plt.imshow(dist_mat, cmap='hot', interpolation='nearest')
plt.show()

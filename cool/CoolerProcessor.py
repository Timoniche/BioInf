import os.path as op

import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas
import h5py

import cooler


def process_cool(filepath):
    c = cooler.Cooler(filepath)
    print(c.info)

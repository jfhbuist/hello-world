# calculate.py

import numpy as np


def do_calculation():
    arr = np.convolve((1, 2, 3), (4, 5, 6))
    mean = np.mean(arr)
    ans = int(mean)
    return ans

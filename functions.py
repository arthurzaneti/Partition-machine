import math

import numpy as np
import matplotlib.pyplot as plt


def calculate_pi(terms):
    n = 1
    pi = 0
    for i in range(1, terms):
        if i % 2 != 0:
            pi += 1 / n
        else:
            pi -= 1 / n
        n += 2
    return pi * 4


def calculate_e(terms):
    e = 0
    for i in range(0, terms):
        e += 1 / math.factorial(i)
    return e


def get_y_ax1(x):
    y = []
    for i in x:
        y.append(calculate_pi(i))
    return y


def get_y_ax2(x):
    y2 = []
    for i in x:
        y2.append(calculate_e(i))
    return y2

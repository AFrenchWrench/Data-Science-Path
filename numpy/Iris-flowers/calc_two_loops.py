# coding: utf-8
import numpy as np
def calc_two_loops(new_points, points):

    # ‌ m is the number of new points (test samples)
    m = len(new_points)
    # n is the number of points (training samples)
    n = len(points)
    # Distance matrix
    d = np.zeros((m, n))

    # For each new point
    for i in range(m):
        # For each point
        for j in range(n):
            # Calculate the distance between the two points
            d[i, j] = np.sum(np.square(new_points[i] - points[j]))

    return d

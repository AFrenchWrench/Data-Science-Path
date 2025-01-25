# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum(
        np.square(new_points[:, np.newaxis, :] - points[np.newaxis, :, :]), axis=2
    )

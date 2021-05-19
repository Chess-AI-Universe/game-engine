import numpy as np
import math

cols = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

def lerf_to_position(lerf):
    row = math.floor(lerf / 8) + 1
    col = cols[lerf % 8]
    return col + str(row)

def lerf_to_bitmap(lerf):
    return np.uint64(2**lerf)

def bitmap_to_lerfs(bitmap):
    res = []
    mask = 1
    for i in range(64):
        if np.uint64(bitmap) & np.uint64(mask):
            res.append(i)
        mask = mask << 1
    return res

def bitmap_to_positions(bitmap):
    lerfs = bitmap_to_lerfs(bitmap)
    return [lerf_to_position(item) for item in lerfs]

def lerf_in_bitmap(lerf, bitmap):
    return (lerf_to_bitmap(lerf) & bitmap) != 0

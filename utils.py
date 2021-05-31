import numpy as np
import math

cols = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])


def index_to_position(index):
    row = math.floor(index / 8) + 1
    col = cols[index % 8]
    return col + str(row)


def position_to_index(position):
    row, col = int(position[1:]), position[:1]
    column = np.where(cols == col)[0][0]
    return 8 * (row - 1) + column


def index_to_bitmap(index):
    return np.uint64(2**index)


def bitmap_to_indexes(bitmap):
    res = []
    mask = 1
    for i in range(64):
        if np.uint64(bitmap) & np.uint64(mask):
            res.append(i)
        mask = mask << 1
    return res


def bitmap_to_positions(bitmap):
    indexes = bitmap_to_indexes(bitmap)
    return [index_to_position(item) for item in indexes]


def index_in_bitmap(index, bitmap):
    return (index_to_bitmap(index) & bitmap) != 0


def north_index(index):
    if index is None or index > 55:
        return None
    return index + 8


def south_index(index):
    if index is None or index < 8:
        return None
    return index - 8


def west_index(index):
    if index is None or (index % 8) == 0:
        return None
    return index - 1


def east_index(index):
    if index is None or ((index + 1) % 8) == 0:
        return None
    return index + 8


def north_west_index(index):
    return north_index(west_index(index))


def north_east_index(index):
    return north_index(east_index(index))


def south_west_index(index):
    return south_index(west_index(index))


def south_east_index(index):
    return south_index(east_index(index))

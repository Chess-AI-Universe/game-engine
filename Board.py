import numpy as np


class Board:
    WHITE = 0
    BLACK = 1

    king = np.array([np.uint(0), np.uint(0)])
    queens = np.array([np.uint(0), np.uint(0)])
    rooks = np.array([np.uint(0), np.uint(0)])
    bishops = np.array([np.uint(0), np.uint(0)])
    knights = np.array([np.uint(0), np.uint(0)])
    pawns = np.array([np.uint(0), np.uint(0)])


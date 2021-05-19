import utils
import numpy as np


class Board:
    BOARD_HEIGHT = 8
    BOARD_WIDTH = 8
    BOARD_SIZE = 64

    WHITE = 0
    BLACK = 1

    KING = 0
    QUEENS = 1
    ROOKS = 2
    BISHOPS = 3
    KNIGHTS = 4
    PAWNS = 5

    def __init__(self):
        self.pieces = np.array([np.array([np.uint64(0x0000000000000010), np.uint64(0x1000000000000000)]),
                                np.array([np.uint64(0x0000000000000008), np.uint64(0x0800000000000000)]),
                                np.array([np.uint64(0x0000000000000081), np.uint64(0x8100000000000000)]),
                                np.array([np.uint64(0x0000000000000024), np.uint64(0x2400000000000000)]),
                                np.array([np.uint64(0x0000000000000042), np.uint64(0x4200000000000000)]),
                                np.array([np.uint64(0x000000000000FF00), np.uint64(0x00FF000000000000)])])

    def print_board(self):
        for i in range(self.BOARD_HEIGHT - 1, -1, -1):
            output = ""
            for j in range(self.BOARD_WIDTH):
                lerf = i * self.BOARD_HEIGHT + j
                if (utils.lerf_in_bitmap(lerf, self.get_white_king())):
                    output += "K"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_king())):
                    output += "k"
                elif (utils.lerf_in_bitmap(lerf, self.get_white_queens())):
                    output += "Q"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_queens())):
                    output += "q"
                elif (utils.lerf_in_bitmap(lerf, self.get_white_rooks())):
                    output += "R"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_rooks())):
                    output += "r"
                elif (utils.lerf_in_bitmap(lerf, self.get_white_bishops())):
                    output += "B"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_bishops())):
                    output += "b"
                elif (utils.lerf_in_bitmap(lerf, self.get_white_knights())):
                    output += "N"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_knights())):
                    output += "n"
                elif (utils.lerf_in_bitmap(lerf, self.get_white_pawns())):
                    output += "P"
                elif (utils.lerf_in_bitmap(lerf, self.get_black_pawns())):
                    output += "p"
                else:
                    output += "."

            print(output)

    def get_white_king(self):
        return self.pieces[self.KING][self.WHITE]

    def get_black_king(self):
        return self.pieces[self.KING][self.BLACK]

    def get_white_queens(self):
        return self.pieces[self.QUEENS][self.WHITE]

    def get_black_queens(self):
        return self.pieces[self.QUEENS][self.BLACK]

    def get_white_rooks(self):
        return self.pieces[self.ROOKS][self.WHITE]

    def get_black_rooks(self):
        return self.pieces[self.ROOKS][self.BLACK]

    def get_white_bishops(self):
        return self.pieces[self.BISHOPS][self.WHITE]

    def get_black_bishops(self):
        return self.pieces[self.BISHOPS][self.BLACK]

    def get_white_knights(self):
        return self.pieces[self.KNIGHTS][self.WHITE]

    def get_black_knights(self):
        return self.pieces[self.KNIGHTS][self.BLACK]

    def get_white_pawns(self):
        return self.pieces[self.PAWNS][self.WHITE]

    def get_black_pawns(self):
        return self.pieces[self.PAWNS][self.BLACK]

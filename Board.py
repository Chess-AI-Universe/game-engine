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
        for row in range(self.BOARD_HEIGHT - 1, -1, -1):
            output = str(row + 1) + '\u2001'
            for col in range(self.BOARD_WIDTH):
                lerf = row * self.BOARD_HEIGHT + col
                if utils.lerf_in_bitmap(lerf, self.get_white_king()):
                    output += "♚"
                elif utils.lerf_in_bitmap(lerf, self.get_black_king()):
                    output += "♔"
                elif utils.lerf_in_bitmap(lerf, self.get_white_queens()):
                    output += "♛"
                elif utils.lerf_in_bitmap(lerf, self.get_black_queens()):
                    output += "♕"
                elif utils.lerf_in_bitmap(lerf, self.get_white_rooks()):
                    output += "♜"
                elif utils.lerf_in_bitmap(lerf, self.get_black_rooks()):
                    output += "♖"
                elif utils.lerf_in_bitmap(lerf, self.get_white_bishops()):
                    output += "♝"
                elif utils.lerf_in_bitmap(lerf, self.get_black_bishops()):
                    output += "♗"
                elif utils.lerf_in_bitmap(lerf, self.get_white_knights()):
                    output += "♞"
                elif utils.lerf_in_bitmap(lerf, self.get_black_knights()):
                    output += "♘"
                elif utils.lerf_in_bitmap(lerf, self.get_white_pawns()):
                    output += "♟"
                elif utils.lerf_in_bitmap(lerf, self.get_black_pawns()):
                    output += "♙"
                else:
                    output += '\u2001'
                output += '\u2002'

            print(output)
        # pls don't look at this unicode space magic
        print('   a\u2007\u2004b\u2007\u2004c\u2007\u2004d\u2007\u2004e\u2007\u2004f\u2007\u2004g\u2007\u2004h')

    def get_white_pieces(self):
        res = np.uint64(0)
        for bitmap in self.pieces:
            res |= bitmap[self.WHITE]
        return res

    def get_black_pieces(self):
        res = np.uint64(0)
        for bitmap in self.pieces:
            res |= bitmap[self.BLACK]
        return res


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

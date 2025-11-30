# import chess

# wrapper on python-chess
# maybe implement some flask endpoints.
import lib_chess


def test_1():


    assert 1 == 1

    board = lib_chess.chess.Board()
    print(board.legal_moves)

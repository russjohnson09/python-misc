
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session

from lib_chess.models import Base, Game
from lib_chess import GameSession

# import chess

# wrapper on python-chess
# maybe implement some flask endpoints.
import lib_chess


# engine = create_engine("sqlite://", echo=True)
engine = create_engine("sqlite:///test.db")



def _reset():
    Base.metadata.drop_all(engine)
    Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    pass

def test_1():


    assert 1 == 1

    board = lib_chess.chess.Board()
    print(board.legal_moves)


def test_create_game_model():
    _reset()

    # board = lib_chess.chess.Board()
    # # Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')
    # board_str = str(board)
    # # create session for engine
    # with Session(engine) as session:
    #     game = Game(
    #         board_str=board_str
    #     )
    #     session.add(game)
    #     # session.add(some_other_object)
    #     session.commit()


    # board_restore =  lib_chess.chess.Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')
    # # search for game

    pass


#  uv run pytest -s -k test_create_game_session
def test_create_game_session():
    _reset()


    gs = GameSession(engine=engine)

    print(gs._board)
    print(gs._board.fen())
    print(gs.uuid)

    gs2 = GameSession(engine=engine, uuid=gs.uuid)

    assert gs2.fen() == 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    assert gs2.move_uci("1") == False

    assert gs2.move_uci("g1f3") == True

    assert gs2.fen() == 'rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1'

    gs3 = GameSession(engine=engine, uuid=gs2.uuid)

    assert gs3.fen() == 'rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1'



def test_flask_controllers():


    pass
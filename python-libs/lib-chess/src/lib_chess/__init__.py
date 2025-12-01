import chess

from .models.game import Game
from sqlalchemy.orm import Session
from sqlalchemy import select


# https://react-chessboard.vercel.app/?path=/docs/how-to-use-options-api--docs#optionsonpiecedrop

class GameSession():
    """Given an engine to work with. Find the id of the game play the game, finish the game etc."""

    _engine: any
    uuid: any
    _board: any
    _game: any

    def __init__(self, engine, uuid: str = None):
        self._engine = engine
        with Session(engine) as session:
            if not uuid:
                board = chess.Board()
                self._board = board

                game = Game(
                    fen=board.fen()
                )
                # self._game = game
                session.add(game)
                session.commit()
                self.uuid = game.uuid
                self._game = game
            else:
                self.uuid = uuid
                # stmt = select(Game).where(Game.uuid == uuid)
                game = session.query(Game).where(Game.uuid == uuid).first()
                # result = session.execute(stmt)
                print(game.uuid)
                self._board = chess.Board(game.fen)
                self._game = game

        pass

    def move_uci(self, move_uci_str: str):
        board = self._board
        try:
            move = chess.Move.from_uci(move_uci_str)

        except:
            return False
        is_legal = move in board.legal_moves
        if not is_legal:
            return False
        with Session(self._engine) as session:
            board.push(move)
            game = self._game
            session.add(game)
            game.fen = board.fen()
            session.commit()

        # move and save move.
        return True
    
    def fen(self):
        return self._board.fen()

    def _get_session():
        pass

    def get_game():

        pass


def start_game():




    pass
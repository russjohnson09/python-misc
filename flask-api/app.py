from flask import Flask,  url_for, redirect, send_from_directory, jsonify
import logging
from sqlalchemy import create_engine, Column, Integer, String

from lib_chess import GameSession
from lib_chess.models.base import Base

logging.basicConfig(level=logging.DEBUG)

engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine)

app = Flask(__name__)

# TODO download from &.wav soundboard
@app.route("/came")
def came():
    return "<p>Hello, World!</p>"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<path:path>')
def static_serve(path):
    print(path)
    app.logger.info(path)

    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory('static', path)


# blueprint chess


@app.route("/chess")
def chess_1():
    return jsonify({'status': 'okay'})

@app.get("/chess/<string:id>")
def chess_by_id(id):
    if id == 'new':
        print('create new session')
        print(GameSession)
        gs = GameSession(engine)
        return jsonify({'status': 'okay', 'uuid': gs.uuid, 'fen': gs.fen()})
    else:
        gs = GameSession(engine, uuid=id)
        return jsonify({'status': 'okay', 'uuid': gs.uuid, 'fen': gs.fen()})

# detect if chess move is legal.
# requires the board state and a move.




# def app(environ, start_response):
#     data = b"Hello, World!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data])



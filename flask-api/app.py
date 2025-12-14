from flask import Flask,  url_for, redirect, send_from_directory, jsonify
import logging
from sqlalchemy import create_engine, Column, Integer, String
from flask_cors import CORS

from lib_chess import GameSession
from lib_chess.models.base import Base

logging.basicConfig(level=logging.DEBUG)

engine = create_engine("sqlite:///test.db")

def _create_tables():

    try:
        Base.metadata.create_all(engine)
    except:
        #sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) table game already exists
        pass
    return

_create_tables()

app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "localhost"}})

# https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
CORS(app)
# Access to fetch at 'https://flask-api.ihateiceforfree.com/chess/349d1547-7d16-45f1-93a6-1c118faab145' from origin 'http://127.0.0.1:8080' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.


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

@app.get("/chess/<string:id>/<string:move>")
def chess_move(id: str, move: str):
    gs = GameSession(engine, uuid=id)
    success = gs.move_uci(move)
    return jsonify({'success': success, 'uuid': gs.uuid, 'fen': gs.fen()})

# detect if chess move is legal.
# requires the board state and a move.




# def app(environ, start_response):
#     data = b"Hello, World!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data])



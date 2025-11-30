from flask import Flask,  url_for, redirect, send_from_directory, jsonify
import logging

logging.basicConfig(level=logging.DEBUG)

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

# detect if chess move is legal.
# requires the board state and a move.




# def app(environ, start_response):
#     data = b"Hello, World!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data])



from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/server')
def websocket(ws):
    print("SOCKET")

@app.route("/")
def hello():
    return "Hello World! 3"

@app.route("/test")
def test():
    return "TEST 1"

if __name__ == "__main__":
    app.run()

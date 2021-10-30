import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
ipAddress = '127.0.0.1'
port = 5000


@app.route('/')
def index():
    return render_template('index.html', ip=ipAddress, port=port)


@socketio.on('connect')
def connect():
    emit('connected')


@socketio.on('start streaming')
def value_changed(message):
    i = 1
    while i <= 100:
        time.sleep(1)
        emit('update value', i)
        i = i + 1


if __name__ == '__main__':
    socketio.run(app, host=ipAddress)

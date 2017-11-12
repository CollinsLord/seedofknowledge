from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Hello world"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('message', namespace='/chat')
def message(message):
    emit('message', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/chat')
def connect():
    emit('response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
    socketio.run(app)
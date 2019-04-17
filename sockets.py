# see: https://flask-socketio.readthedocs.io/en/latest/

from flask import Flask
from flask import render_template

from flask_socketio import emit
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('sockets.html')


@socketio.on('count')
def handle_message(message):
    print(message)
    # time.sleep(1)
    message['counter'] += 1
    emit('message', message)


@socketio.on('on_text_change')
def handle_my_custom_event(json):
    print(json)
    json['text'] = json['text'] * 2
    emit('change text', json)


if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)

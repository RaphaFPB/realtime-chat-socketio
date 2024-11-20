from flask import Flask,render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def chat_page():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    data = json.loads(msg)
    username = data['user']
    message = data['text']
    emit('message', {'user': username, 'text': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
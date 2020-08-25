from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def mensaje(msg):
    print("Mensaje: " + msg)
    send(msg, broadcas = True)

if __name__ == '__main__':
    socketio.run(app)
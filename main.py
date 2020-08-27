from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')

@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send(data)
    emit('some', 'Este es un mensaje de un evento custom')

if __name__ == "__main__":
    socketio.run(app, debug = True)
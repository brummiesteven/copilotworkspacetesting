import requests
import random
from flask import Flask, render_template, request, redirect
from flask_material import Material
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
Material(app)
socketio = SocketIO(app)

players = []  # List to track joined players

def fetch_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    data = response.json()
    return data['results']

@app.route('/', methods=['GET', 'POST'])
def get_user_name():
    if request.method == 'POST':
        name = request.form['name']
        players.append(name)
        if len(players) >= 2:
            socketio.emit('start_game')
        return render_template('wait.html', name=name)
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def ask_questions():
    if request.method == 'POST':
        answers = request.form.getlist('answers')
        questions = fetch_questions()
        score = 0
        if len(answers) == len(questions):
            for i, question in enumerate(questions):
                if question['correct_answer'] == answers[i]:
                    score += 1
        return render_template('result.html', score=score)
    questions = fetch_questions()
    return render_template('quiz.html', questions=questions)

@socketio.on('join')
def handle_join(data):
    players.append(data['name'])
    if len(players) >= 2:
        emit('start_game', broadcast=True)
    else:
        emit('player_joined', data, broadcast=True)

@socketio.on('submit_answers')
def handle_submit_answers(data):
    player_scores = data['scores']
    emit('compare_scores', player_scores, broadcast=True)

def main():
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

if __name__ == "__main__":
    main()

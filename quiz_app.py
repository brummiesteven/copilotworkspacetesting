import requests
import random
from flask import Flask, render_template, request, redirect
from flask_material import Material
from flask_socketio import SocketIO, emit

app = Flask(__name__)
Material(app)
socketio = SocketIO(app)

def fetch_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    data = response.json()
    return data['results']

@app.route('/', methods=['GET', 'POST'])
def get_user_name():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(f'/quiz?name={name}')
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
    emit('player_joined', data, broadcast=True)

@socketio.on('submit_answers')
def handle_submit_answers(data):
    player_scores = data['scores']
    emit('compare_scores', player_scores, broadcast=True)

def main():
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()

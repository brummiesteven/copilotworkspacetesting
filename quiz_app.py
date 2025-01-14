import requests
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
        for i, question in enumerate(questions):
            if question['correct_answer'] == answers[i]:
                score += 1
        return render_template('result.html', score=score)
    questions = fetch_questions()
    return render_template('quiz.html', questions=questions)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

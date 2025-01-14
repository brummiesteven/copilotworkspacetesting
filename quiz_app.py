import requests
import random

def fetch_questions():
    response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    data = response.json()
    return data['results']

def get_user_name():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name

def ask_questions(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)
        for j, option in enumerate(options):
            print(f"{j+1}. {option}")
        answer = int(input("Your answer (1-4): "))
        if options[answer-1] == question['correct_answer']:
            score += 1
    return score

def main():
    user_name = get_user_name()
    questions = fetch_questions()
    score = ask_questions(questions)
    print(f"{user_name}, your score is {score}/10")

if __name__ == "__main__":
    main()

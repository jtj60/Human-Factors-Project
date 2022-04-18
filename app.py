from flask import Flask, render_template, request, redirect
from flask_bootstrap5 import Bootstrap
import csv

from quiz_brain import QuizBrain
from question_model import Question


app = Flask(__name__)
user = []

with open('majors.csv') as f:
    majors = [{x: str(y) for x, y in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

# question_bank = []
# question_data = {}

# for question in question_data:
#     question_text = question['text']
#     question_answer = question['answer']
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')
    
@app.route('/majors')
def majors():
    return render_template('major.html')

# if __name__ == '__app__':
#     create_app().run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap5 import Bootstrap
import csv
import json
app = Flask(__name__)

def update_scores(scores, value, Major):
    for x in scores:
        if x["Major"] == Major:
            x["Score"] += value
            return scores

def parse_csv(csv_name):
    with open(csv_name) as f:
        return_list = [{x: str(y) for x, y in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
        return return_list

def get_top_3(results):
    n = 3
    cut = results[n:]
    return results

@app.route('/')
def index():
    majors = parse_csv('majors.csv')
    return render_template('index.html', majors = majors)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    majors = parse_csv('majors.csv')
    questions = parse_csv('questions.csv')

    scores = []
    for m in majors:
        temp = {'Major': m["Major"], "Score": 0}
        scores.append(temp)
    
    if request.method == 'POST':
        q0 = int(request.form.get('question0'))
        q1 = int(request.form.get('question1'))
        q2 = int(request.form.get('question2'))
        q3 = int(request.form.get('question3'))
        q4 = int(request.form.get('question4'))
        q5 = int(request.form.get('question5'))
        q6 = int(request.form.get('question6'))
        q7 = int(request.form.get('question7'))

        for i, q in enumerate(questions):
            if i == 0:
                update_scores(scores, q0, 'Accounting')
                update_scores(scores, q0, 'Business Administration')
                update_scores(scores, q0, 'Finance')
                update_scores(scores, q0, 'Marketing')
            if i == 1:
                update_scores(scores, q1, 'Computer Science')
                update_scores(scores, q1, 'Information Science')
                update_scores(scores, q1, 'Mathematics and Statistics')
            if i == 2:
                update_scores(scores, q2, 'Accounting')
                update_scores(scores, q2, 'Civil Engineering')
                update_scores(scores, q2, 'Computer Science')
                update_scores(scores, q2, 'Finance')
                update_scores(scores, q2, 'Information Science')
                update_scores(scores, q2, 'Mathematics and Statistics')
                update_scores(scores, q2, 'Systems Engineering')
            if i == 3:
                update_scores(scores, q3, 'Medical Assisting')
                update_scores(scores, q3, 'Nursing')
                update_scores(scores, q3, 'Physical Therapy')
                update_scores(scores, q3, 'Psychology')
            if i == 4:
                update_scores(scores, q4, 'Culinary Arts')
            if i == 5:
                update_scores(scores, q5, 'Culinary Arts')
                update_scores(scores, q5, 'Nursing')
                update_scores(scores, q5, 'Physical Therapy')        
            if i == 6:
                update_scores(scores, q6, 'Business Administration')
                update_scores(scores, q6, 'Marketing')
                update_scores(scores, q6, 'Instructional Design')
                update_scores(scores, q6, 'Systems Engineering')         
            if i == 7:
                update_scores(scores, q7, 'Civil Engineering')
                update_scores(scores, q7, 'Instructional Design')
                update_scores(scores, q7, 'Medical Assisting')

        results = sorted(scores, key=lambda x: x['Score'], reverse = True)
        print(results)
        results = get_top_3(results)
        m0 = str(results[0]['Major'])
        m1 = str(results[1]['Major'])
        m2 = str(results[2]['Major'])
        return redirect(url_for('results', m0=m0, m1=m1, m2=m2))

    return render_template('quiz.html', questions = questions, scores = scores)
    
@app.route('/majors/<string:name>')
def majors(name):
    majors = parse_csv('majors.csv')
    for m in majors:
        if name == m['Major']:
            major = m
    return render_template('major.html', major = major)

@app.route('/results/<string:m0>/<string:m1>/<string:m2>')
def results(m0, m1, m2):
    results = []
    majors = parse_csv('majors.csv')
    for m in majors:
        if m0 == m['Major'] or m1 == m['Major'] or m2 == m['Major']:
            results.append(m)
    return render_template('results.html', results = results)
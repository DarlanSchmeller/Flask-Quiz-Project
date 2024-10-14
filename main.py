from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

app.secret_key = 'your_unique_secret_key' 

quiz_data = [
    [
        {"question": "O céu é azul?", "answer": "correct"},
        {"question": "2 + 2 é igual a 5?", "answer": "wrong"},
    ],
    [
        {"question": "Python é uma linguagem de programação?", "answer": "correct"},
        {"question": "HTML é uma linguagem de programação?", "answer": "wrong"},
    ],
    [
        {"question": "Flask é um framework web?", "answer": "correct"},
        {"question": "Java é uma cobra?", "answer": "wrong"},
    ],
    [
        {"question": "A água é molhada?", "answer": "correct"},
        {"question": "O fogo é frio?", "answer": "wrong"},
    ],
    [
        {"question": "Os gatos latem?", "answer": "wrong"},
        {"question": "Os cães abanam o rabo?", "answer": "correct"},
    ],
]




@app.route('/')
def index():
    session['score'] = 0
    session['level'] = 0

    return render_template('quiz.html')



@app.route('/quiz')
def quiz():
    level = session.get('level', 0)
    if level < len(quiz_data):
        return render_template('quiz.html', quiz_data=quiz_data[level], level=level)
    else:
        return redirect(url_for('result'))


@app.route('/submit', methods=['POST'])
def submit():
    level = session.get('level', 0)
    score = session.get('score', 0)


    for i, question in enumerate(quiz_data[level]):

        user_answer = request.form.get(f'question-{i}')

        if user_answer == question['answer']:
            score += 1


    session['score'] = score
    session['level'] = level + 1  # Move to the next level

    return redirect(url_for('quiz'))


@app.route('/result')
def result():
    score = session.get('score', 0)
    total = sum(len(level) for level in quiz_data)  # Total questions across all levels
    return render_template('result.html', score=score, total=total)



if __name__ == '__main__':
    app.run(debug=True)

# Import libraries
from flask import Flask, request, render_template
from predict import run_prediction

#load model
model_path = './cuad-models/roberta-base/'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_form():
    if request.method == 'POST':
        questions = request.form.getlist('questions')
        context = request.form.get('context')

        print(f"Selected questions: {questions}")  # print selected questions

        if not questions:  # check if any question was selected
            print("No questions were selected")
            return render_template('predict.html')

        answers = {}
        for question in questions:
            answer = run_prediction([question], context, model_path=model_path)
            answers[question] = answer[list(answer.keys())[0]]  # get the answer of the first question in 'answer' dictionary

        return render_template('result.html', questions=questions, answers=answers)

    all_questions = []
    with open('questions.txt', 'r', encoding='utf8') as f:
        for line in f:
            question_number, question_text = line.strip().split(": ", 1)
            all_questions.append(question_text)
    return render_template('predict.html', questions=all_questions)

if __name__ == '__main__':
    app.run(debug=True)

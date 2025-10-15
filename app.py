from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('number1', type=float)
        num2 = request.form.get('number2', type=float)
        result = num1 + num2
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
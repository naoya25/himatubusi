from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        if request.form["input_text"] == "":
            return render_template("index.html")
        else:
            sp.var('x')
            text = sp.solve(request.form["input_text"], x)
            print(text)
            return render_template('index.html', kai=text, siki=f'{request.form["input_text"]}の解')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


# submit name and age
@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def process_query(q):
    if q == "What is your name?":
        return "Computing genius"

    elif q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"

    elif "plus" in q:  
        numbers = re.findall(r'\d+', q)         
        if len(numbers) == 2:         
            num1, num2 = int(numbers[0]), int(numbers[1])            
            result = num1 + num2          
            return f"{result}"
    

    else:
        return "Unknown"


# get the dinosaurs
@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    response = process_query(q)

    return response

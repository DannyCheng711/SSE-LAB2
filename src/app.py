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
        numbers = re.findall(r"\d+", q)
        if len(numbers) == 2:
            num1, num2 = int(numbers[0]), int(numbers[1])
            result = num1 + num2
            return f"{result}"

    elif "largest" in q:

        numbers = re.findall(r"\d+(?:\.\d+)*", q)

        # 解析每个数字的最大子数
        if numbers:
            max_value = None
            for num in numbers:
                sub_values = [float(part) for part in num.split(".")]
                largest_sub_value = max(sub_values)

                if max_value is None or largest_sub_value > max_value:
                    max_value = largest_sub_value
            return (
                str(int(max_value))
                if max_value.is_integer()
                else str(max_value)
            )

    else:
        return "Unknown"


# get the dinosaurs
@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    response = process_query(q)

    return response

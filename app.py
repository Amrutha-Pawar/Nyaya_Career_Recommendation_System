from flask import Flask, render_template, request
from inference import infer_career

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    recommendations = []

    if request.method == "POST":

        student_inputs = request.form.getlist("skills")

        recommendations = infer_career(student_inputs)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
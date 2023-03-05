from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def personal():
    return render_template("personal.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/instruction")
def instruction():
    return render_template("instruction.html")


@app.route("/main_function")
def main_instruction():
    return render_template("main_function.html")


if __name__ == "__main__":
    app.run(debug=True)

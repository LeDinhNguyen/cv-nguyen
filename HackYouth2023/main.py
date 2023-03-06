from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def personal():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/instruction")
def instruction():
    return render_template("instruction.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

from pymongo import MongoClient
from flask import Flask, render_template

app = Flask("__name__")

client = MongoClient("localhost", 27017)
db = client["flask_db"]
project = db["project"]


@app.route("/")
def home():
    return render_template("about.html")

@app.route("")


@app.route("/about")
def teamInformation():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


@app.route('/feature_1')
def feature_1():
    return '<h1>Feature 1 deployed!</h1>'


@app.route('/feature_2')
def feature_2():
    return '<h1>Feature 2 deployed!</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)

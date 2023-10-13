from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello, Duniyaaaaaaaa</p>"


@app.route("/username/<name>")
def greet(name):
    return f"Hello There {name}!!"


if __name__ == "__main__":
    app.run(debug=True)

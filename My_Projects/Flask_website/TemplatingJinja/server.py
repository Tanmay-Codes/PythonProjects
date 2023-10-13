from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/guests/<user>")
def home(user):
    date = datetime.datetime.now().year
    return render_template("index.html", today=date, name=user)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)

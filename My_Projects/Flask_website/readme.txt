(server.py)

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
   return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)



[A]. Rendering html files as template:

1) add a new directory called templates, and keep all the html code in this directory.
2) Now import render_template from flask and call the method render_template('index.html')
3) note all the CSS and related Assets(images) need to be kept into another directory named static.


[B] Using the template for making website: (https://html5up.net  or squarespace) for free online template to use.

in order to edit the website in the browser:
go to the console and add a command:
document.body.contentEditable=true





from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    currentTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return render_template("index.html", name='Payas', currentTime=currentTime)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

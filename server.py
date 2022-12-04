from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("url").startswith("http"):
            return redirect(request.form.get("url"))
        else:
            return redirect("https://google.com/search?q={}".format(request.form.get("url")))
    return render_template("home.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/game/<page>")
def game(page):
    if page == "atari2600":
        return render_template("atari.html")
    elif page == "snake":
        return render_template("snake.html")
    elif page == "test":
        return "This is a test"

@app.route("/ux")
def ux():
    return render_template("download.html")

@app.route("/pong")
def pong():
    return render_template("pong.html")
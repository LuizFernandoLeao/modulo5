# app.py
from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)

dbecho = TinyDB("echo.json")
dbping = TinyDB("ping.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/echo", methods=["GET", "POST"])
def novo(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        dbecho.insert({"nome": nome})
    posts = dbecho.all()
    return render_template("echo.html", nome=nome, posts=posts)

@app.route("/ping")    
def ping():
    return jsonify(dbping.all())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
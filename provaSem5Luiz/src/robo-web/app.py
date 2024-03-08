from flask import Flask, render_template, request
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB("caminhos.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novo", methods=["GET", "POST"])
def novo(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
    return render_template("novo.html", nome=nome)

@app.route("/pegar_caminho", methods=["GET", "POST"])
def pegar_caminho(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert({"nome": nome})
    posts = db.all()
    return render_template("pegar_caminho.html", nome=nome, posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

elementos = [
    {'id': 1, 'nome': 'Elemento 1'},
    {'id': 2, 'nome': 'Elemento 2'},
    {'id': 3, 'nome': 'Elemento 3'},
    {'id': 4, 'nome': 'Elemento 4'},
    {'id': 5, 'nome': 'Elemento 5'},
    {'id': 6, 'nome': 'Elemento 6'},
    {'id': 7, 'nome': 'Elemento 7'},
    {'id': 8, 'nome': 'Elemento 8'},
    {'id': 9, 'nome': 'Elemento 9'},
    {'id': 10, 'nome': 'Elemento 10'},
]

# Retorna o index.html
@app.route('/')
def index():
    return render_template('index.html')


# Retorna a base do header com o HTMX
@app.route('/pegar-header')
def pegar_header():
    return '<header id="header">Header</header>'

# Retorna um conjunto de elementos no formato de uma lista de cards
@app.route('/pegar-elementos')
def pegar_elementos():
    return render_template('elementos.html', elementos=elementos)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
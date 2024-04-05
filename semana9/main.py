# Importação das bibliotecas
from flask import Flask, render_template, request
from flask_cors import CORS
from tinydb import TinyDB
from pydobot import Dobot

app = Flask(__name__)

# Banco de dados
db = TinyDB('logs.json')

CORS(app)

# Conexão com o robo
try:
    robo = Dobot(port='COM3')
    robo.speed(100)
    print("Conectado com o robô")
except:
    robo = None
    print(f"Erro ao conectar com o robô")

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

# Tela Inicial 
@app.route('/')
def index():
    # Robo desconectado
    if robo is None:
        return'<h2>Conecte o robô, ou entre na rota /log<h2>'
    return render_template('index.html')

# Robo conectado
if robo is not None:
    
    # Header
    @app.route('/pegar-header')
    def pegar_header():
        return '<header id="header">Header</header>'

    # Elementos
    @app.route('/pegar-elementos')
    def pegar_elementos():
        return render_template('elementos.html', elementos=elementos)

    @app.route('/controlar', methods=['POST'])
    def mover():
        if request.method == 'POST':
            x = request.args.get('x')
            y = request.args.get('y')
            z = request.args.get('z')
            r = request.args.get('r')
            robo.move_to(float(x),float(y),float(z),float(r))
            return f'<h2>X: {x}, Y: {y}, Z: {z}</h2>'
    
    @app.route('/posicao')
    def posicao():
        db.insert({'log': 'GET da /posicao'})
        return f'<h2>{robo.pose()}<h2>'
    
    @app.route('/print')
    def printar():
        db.insert({'log':'GET na /print'})
        return '<h2>print</h2>'
    
@app.route('/log')
def exibir_logs():
    logs = db.all()
    print(logs)
    return render_template('logs.html', logs=logs)
   
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
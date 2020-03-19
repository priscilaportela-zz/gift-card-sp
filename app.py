# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/formulario")
def shoelaces():
    return 'direcionar para link de formlulario para insercao de novos negócios'

@app.route("/sobre nós")
def about():
    return 'Inserir link para twitter, intagram...'

@app.route('/como-obter-lat-lng')
    return 'Ensinar as pessoas como obter a latitude e longitude do seu lugar preferido'

if __name__ == '__main__':
    app.run(debug=True)

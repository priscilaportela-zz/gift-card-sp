# app.py
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/formulario')
def form():
    return redirect('https://forms.gle/7KWhBWsm2nFJqMFA9', code=302)

@app.route('/sobre')
def about():
    return 'Inserir link para twitter, intagram...'

@app.route('/como-obter-lat-lng')
def info():
    return redirect("https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=pt-BR", code=302)

if __name__ == '__main__':
    app.run(debug=True)

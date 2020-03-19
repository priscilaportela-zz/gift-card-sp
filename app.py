# app.py
from flask import Flask, render_template, redirect
import webbrowser

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/formulario')
def form():
    return webbrowser.open_new_tab('https://forms.gle/7KWhBWsm2nFJqMFA9')

@app.route('/sobre')
def about():
    return 'Inserir link para twitter e github...'

@app.route('/como-obter-lat-lng')
def info():
    return webbrowser.open_new_tab('https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=pt-BR')

if __name__ == '__main__':
    app.run(debug=True)

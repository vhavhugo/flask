from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    frutas = ["Morango", "Uva", "Laranja", "Manga", "Pêra", "Melão"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno":8.0}
    return render_template('sobre.html', notas=notas)

#http://127.0.0.1:5000
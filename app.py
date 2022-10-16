#from crypt import methods
from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def principal():
    #frutas = ["Morango", "Uva", "Laranja", "Manga", "Pêra", "Melão"]
    
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno":8.0}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    
    return render_template('sobre.html', registros=registros)


@app.route('/filmes')
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])


if __name__=="__main__":
    app.run(debug=True)
#http://127.0.0.1:5000
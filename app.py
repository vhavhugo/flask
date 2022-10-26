#from crypt import methods
from flask import Flask, render_template, request
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

db = SQLAlchemy(app)

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


@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2014&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    elif propriedade == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594"
    
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])


if __name__=="__main__":
    # app.run(debug=True)
    db.init_app(app)
#http://127.0.0.1:5000
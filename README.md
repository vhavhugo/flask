# flask

# Criar uma variável de ambiênte
set FLASK_APP=app.py
flask run

# http://127.0.0.1:5000

# Mudar para ambiente de desenvolvimento
set FLASK_ENV=development

# Colocando esse código no app.py na ultima linha, não precisa mais usar o set FLASK_ENV=development toda vez que fechar e abrir o terminal.

if __name__=="__main__":
    app.run(debug=True)


# api_TMDB
Exemplo de Requisição de API

https://api.themoviedb.org/3/movie/550?api_key=acff65ba7f73c32ae962dcc8dd6de594

https://image.tmdb.org/t/p/w500//rr7E0NoGKxvbkb89eR1GwfoYjpA.jpg

/discover/movie?sort_by=popularity.desc

# Filmes mais populares
https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594

# Filmes mais populares para crianças
https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594


# Filmes 2010
https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594

# Filmes drama
https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2014&api_key=acff65ba7f73c32ae962dcc8dd6de594

# tom cruize
https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=acff65ba7f73c32ae962dcc8dd6de594


- Filmes + Populares
- Filmes Kids
- Filmes 2010
- Filmes Drama
- Tom Cruize

# MYSQL
https://dev.mysql.com/downloads/file/?id=514518


# Colocar no path do windows
C:\Program Files\MySQL\MySQL Server 8.0\bin

# no prompt
mysql -u root -p



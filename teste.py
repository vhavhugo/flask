import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc?api_key=acff65ba7f73c32ae962dcc8dd6de594"

resposta = urllib.request.urlopen(url)

print(resposta)



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


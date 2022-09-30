from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return "<h1>Hello World</h1>"
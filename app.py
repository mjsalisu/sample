from flask import Flask

app = Flask(__name__)

@app.post('/')
def post():
    return 'Hello, World from POST!'

@app.get('/')
def get():
    return 'Hello, World from GET!'

@app.patch('/')
def patch():
    return 'Hello, World from PATCH!'

@app.delete('/')
def delete():
    return 'Hello, World from DELETE!'
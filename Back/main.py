from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get('/user')
def get():
    return 'Fonction GET all'

@app.get('/user/id')
def getUser():
    return 'Fonction GET user'

@app.post('/user')
def postUser():
    return 'Fonction POST'
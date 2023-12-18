from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.get('/user')
def get():
    return 'Fonction GET all'

@app.get('/user/id')
def getUser():
    return 'Fonction GET user'

@app.post('/user')
def postUser():
    return 'Fonction POST'
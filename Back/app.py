from flask import Flask, render_template

from Routes.user import user_route
from Routes.sonde import sonde_route
from Routes.releve import releve_route

app = Flask(__name__, template_folder='../Front')

app.register_blueprint(user_route)
app.register_blueprint(sonde_route)
app.register_blueprint(releve_route)


@app.route("/")
def hello_world():
    return render_template("index.html")


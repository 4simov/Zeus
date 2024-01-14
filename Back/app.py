from flask import Flask, render_template
from flask_restx import Api
from Database.db_connexion import db
from Controller.userController import user_route
from Controller.sondeController import sonde_route
from Controller.releveController import releve_route
from Controller.generateController import generate_route
from flask_cors import CORS

app = Flask(__name__, template_folder='../Front')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meteo.db'  # Chemin vers la base de données SQLite

api = Api(app, version='1.0', title='Mon API', description='Description de mon API')

app.register_blueprint(user_route)
app.register_blueprint(sonde_route)
app.register_blueprint(releve_route)
app.register_blueprint(generate_route)

db.init_app(app)
with app.app_context():
    db.create_all()


    
@app.route("/home")
def hello_world():
    return render_template("index.html")


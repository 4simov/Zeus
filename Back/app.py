from flask import Flask, render_template
from flask_restx import Api
from Database.db_connexion import db
from Controller.userController import user_route
from Controller.sondeController import sonde_route
from Controller.releveController import releve_route
from Controller.generateController import generate_route

app = Flask(__name__, template_folder='../Front')
api = Api(app, version='1.0', title='Mon API', description='Description de mon API')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meteo.db'  # Chemin vers la base de données SQLite

app.register_blueprint(user_route)
app.register_blueprint(sonde_route)
app.register_blueprint(releve_route)
app.register_blueprint(generate_route)

db.init_app(app)
with app.app_context():
    db.create_all()


    
@app.route("/")
def hello_world():
    return render_template("index.html")


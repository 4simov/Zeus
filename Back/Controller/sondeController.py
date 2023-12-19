from flask import Blueprint
from Database.db_connexion import db
from Models.sondeModel import db as sonde_db, Sonde
sonde_route = Blueprint('sonde', __name__)

class Sonde() :
    @sonde_route.get('/sonde')
    def get():
        return 'Fonction GET all sonde'

    @sonde_route.get('/sonde/id')
    def get_user():
        return 'Fonction GET sonde'

    @sonde_route.post('/sonde')
    def post_user():
        return 'Fonction POST sonde'
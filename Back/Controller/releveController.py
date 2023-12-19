from flask import Blueprint
from Database.db_connexion import db
from Models.releveModel import db as releve_db, Releve

releve_route = Blueprint('releve', __name__) 

class Releve() :   
    @releve_route.get('/releve')
    def get():
        return "releves iyfjyfjf"

    @releve_route.get('/releve/id')
    def get_user():
        return 'Fonction GET relevé'

    @releve_route.post('/releve/id')
    def post_user():
        return 'Fonction POST relevé'
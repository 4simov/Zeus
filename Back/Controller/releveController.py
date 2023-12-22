from flask import Blueprint, request, json
from Database.db_connexion import db
from Models.releveModel import Releve

releve_route = Blueprint('releve', __name__) 

class Releve() :   
    @releve_route.get('/releve')
    def get():
        return "releves iyfjyfjf"

    @releve_route.get('/releve/id')
    def get_user():
        return 'Fonction GET relevé'

    @releve_route.post('/re')
    def post_user():
        if request.is_json:
            data = request.json
            re = Releve(data.get('temperature'), data.get('humidite'))
            #re.temperature = data.get('temperature')
            #re.humidite = data.get('humidite')
            #db.session.add(re)
            #db.session.commit()
            return {'message': 'Données générées avec succès.'}, 201
        else:
            return 'Format not support'

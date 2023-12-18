from flask import Blueprint

releve_route = Blueprint('releve', __name__)

@releve_route.get('/releve')
def get():
    return 'Fonction GET all sonde'

@releve_route.get('/releve/id')
def get_user():
    return 'Fonction GET relevé'

@releve_route.post('/releve/id')
def post_user():
    return 'Fonction POST relevé'
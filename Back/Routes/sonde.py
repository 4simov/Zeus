from flask import Blueprint

sonde_route = Blueprint('sonde', __name__)

@sonde_route.get('/sonde')
def get():
    return 'Fonction GET all sonde'

@sonde_route.get('/sonde/id')
def get_user():
    return 'Fonction GET sonde'

@sonde_route.post('/sonde')
def post_user():
    return 'Fonction POST sonde'
from flask import Blueprint

user_route = Blueprint('user', __name__)

@user_route.get('/user')
def get():
    return 'Fonction GET all'

@user_route.get('/user/id')
def get_user():
    return 'Fonction GET user'

@user_route.post('/user')
def post_user():
    return 'Fonction POST'
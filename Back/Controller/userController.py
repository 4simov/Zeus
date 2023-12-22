from flask import Blueprint
from Database.db_connexion import db
from Models.userModel import db as user_db, User
user_route = Blueprint('user', __name__)

class User() :    
    @user_route.get('/user')
    def get():
        return 'Fonction GET all'

    @user_route.get('/user/id')
    def get_user():
        return 'Fonction GET user'

    @user_route.post('/user')
    def post_user():
        return 'Fonction POST'
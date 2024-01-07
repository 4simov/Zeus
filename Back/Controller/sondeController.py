from flask import Blueprint
from Database.db_connexion import db
from Models.sondeModel import db as sonde_db, Sonde
sonde_route = Blueprint('sonde', __name__)

class SondeController() :
    @sonde_route.get('/sonde')
    def get():
        return 'Fonction GET all sonde'

    @sonde_route.get('/sonde/id')
    def get_user():
        return 'Fonction GET sonde'

    @sonde_route.post('/sonde/<idS>')
    def post_sonde(idS):
        if Sonde.query.get(idS) is None:
            s = Sonde(
                id = idS,
                activate = True
            )
            db.session.add(s)
            db.session.commit()
            return 'Fonction POST sonde'
        else :
            print("already exist")          
            return "already exist"
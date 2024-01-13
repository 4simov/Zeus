from flask import Blueprint, jsonify, request
from Database.db_connexion import db
from Models.sondeModel import db as sonde_db, Sonde
sonde_route = Blueprint('sonde', __name__)

class SondeController() :
    @sonde_route.get('/sonde')
    def get():
        return 'Fonction GET all sonde'

    @sonde_route.get('/sonde/<idS>')
    def get_by_id(idS):
        s = Sonde.query.get(idS)
        if s :
            return s.to_json()
        else :
            return 'Pas de sonde associées à cette id'

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
        
    @sonde_route.put('/sonde/<idS>')
    def update_sonde(idS) :
        s = Sonde.query.get(idS)
        if s is None:
            return "Cette sonde n'existe pas"
        else :
            if request.is_json:
                print(str(request.get_json("activation")))
                s.activate = request.get_json("activation")
            else :
                return "il manque des paramètres dans le json"
            db.session.commit()
            return s.to_json()
    
    @sonde_route.put('/sonde/<idS>/close')
    def close_sonde(idS) :
        s = Sonde.query.get(idS)
        if s is None:
            return "Cette sonde n'existe pas"
        else :
            if request.is_json:
                s.activate  = False
                
            else :
                return "il manque des paramètres dans le json"
            db.session.commit()
            return s.to_json()
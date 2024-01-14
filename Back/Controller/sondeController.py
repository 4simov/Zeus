from flask import Blueprint, jsonify, request
from Database.db_connexion import db
from Models.sondeModel import db as sonde_db, Sonde
sonde_route = Blueprint('sonde', __name__)

class SondeController() :
    @sonde_route.get('/sonde')
    def get():
        sondes = Sonde.query.all()
        return jsonify([s.to_json() for s in sondes])
        #return jsonify({ 'Sonde' : [s.to_json() for s in sondes]})

    @sonde_route.get('/sonde/<idS>')
    def get_by_id(idS):
        s = Sonde.query.get(idS)
        if s :
            rep = s.to_json()
            print(rep)
            return rep
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
                s.activate = request.json.get("activation")
            else :
                return "il manque des paramètres dans le json"
            db.session.add(s)
            db.session.commit()
            return s.to_json()
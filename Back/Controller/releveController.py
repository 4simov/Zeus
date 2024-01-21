from sqlalchemy import desc, text
from Database.db_connexion import db
from Models.releveModel import Releve
from flask import Blueprint, abort, request, jsonify
import datetime
releve_route = Blueprint('releve', __name__) 

class ReleveController() :   
    @releve_route.get('/releve')
    def get():
        re = Releve.query.all()
        return jsonify([r.to_json() for r in re])

    @releve_route.get("/releve/<idR>")
    def get_releve(idR):
        re = Releve.query.get(idR)
        response = re.to_json() 
        return response

    @releve_route.get("/releve-by-sonde/<idS>")
    def get_releveBySonde(idS):
        re = Releve.query.filter_by(sonde_id = idS).order_by(Releve.date)
        response = [r.to_json() for r in re]
        return response

    @releve_route.post('/re')
    def post_releve():
        db.session.execute(text("pragma foreign_keys=on"))
        if request.is_json:
            data = request.json
            print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", data.get('humidite'));
            re = Releve(sonde_id = data.get('sonde_id'), temperature = data.get('temperature'), humidite = data.get('humidite'), date = data.get("date"))
            
            #re.temperature = data.get('temperature')
            #re.humidite = data.get('humidite')
            db.session.add(re)
            db.session.commit()
            return {'message': 'Données générées avec succès.'}, 201
        else:
            return 'Format not support'
    
    @releve_route.delete("/releve/<idR>")
    def delete_releve(idR):
        re = Releve.query.get(idR)
        if re is None :
            abort(404)
        db.session.delete(re)
        db.session.commit()
        return re.to_json()
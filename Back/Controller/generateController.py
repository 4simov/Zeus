from Database.db_connexion import db
from Controller.sondeController import Sonde
from Models.releveModel import Releve
from Models.userModel import User
from datetime import datetime, date, time
from flask import Blueprint

generate_route = Blueprint('generate', __name__)

class Generate():
    @generate_route.get('/generate')
    def postInit():
        # Vérifiez si la base de données est vide
        if (db.session.query(User).all() or
           db.session.query(Releve).all()):
            return {'message': 'La base de données n\'est pas vide. Aucune donnée générée.'}, 200

        # Générez 10 utilisateurs et 10 données météorologiques
        for i in range(10):
            new_user = User(
                name=f'Nom{i}',
                mail=f'user{i}@example.com',
                password=f'password{i}'
            )
            db.session.add(new_user)

            new_weather = Releve(
                temperature=25.0 + i,
                humidite=50.0 + i
            )
            db.session.add(new_weather)

        db.session.commit()

        return {'message': 'Données générées avec succès.'}, 201
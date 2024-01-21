from Database.db_connexion import db
from Models.sondeModel import Sonde
db = db

class Releve(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    sonde_id = db.Column(db.String, db.ForeignKey('sonde.id'), nullable = False)
    temperature = db.Column(db.Float)
    humidite = db.Column(db.Float)
    date = db.Column(db.String)

    def to_json(self):
        return {
            'id': self.id,
            'idSonde': self.sonde_id,
            'temperature': self.temperature,
            'humidite': self.humidite,
            'date': self.date
        }

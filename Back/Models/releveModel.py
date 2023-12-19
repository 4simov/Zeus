from Database.db_connexion import db

db = db

class Releve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #idSonde = db.Column(db.Integer, foreign_key =False)
    temperature = db.Column(db.Float)
    humidite = db.Column(db.Float)
    ##date = db.Column(db.Date)
    ##heure = db.Column(db.Time)
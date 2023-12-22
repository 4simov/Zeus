from Database.db_connexion import db

db = db

class Sonde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
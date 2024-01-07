from Database.db_connexion import db

db = db

class Sonde(db.Model):
    id = db.Column(db.String, primary_key=True, nullable = False)
    activate = db.Column(db.Boolean)
    sonde = db.relationship('Releve', backref='sonde', lazy = True)
from Database.db_connexion import db

db = db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    mail = db.Column(db.String(30))
    password = db.Column(db.String(100))
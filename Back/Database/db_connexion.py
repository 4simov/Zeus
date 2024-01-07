from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, text

DATABASE = 'db_meteo.db'

db = SQLAlchemy()



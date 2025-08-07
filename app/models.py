from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
        id = db.Column(db.Integer ,primary_key=True)
        username = db.Column(db.String(10), nullable=False)
        email = db.Column(db.String(50), nullable=False)
        password = db.Column(db.String(50), nullable=False)
        estatus = db.Column(db.String(25))
        fecha_registro = db.Column(db.DateTime, default=datetime.now)
        vacantes = db.relationship('Vacante')

class Vacante(db.Model):
        id = db.Column(db.Integer ,primary_key=True)
        nombre = db.Column(db.String(100), nullable=False)
        descripcion = db.Column(db.Text, nullable=False)
        detalle = db.Column(db.Text)
        fecha_publicacion = db.Column(db.DateTime, default=datetime.now)
        id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
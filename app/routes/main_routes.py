from flask import Blueprint, render_template, session, redirect, url_for, flash
from ..models import Usuario, Vacante

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    vacantes = Vacante.query.order_by(Vacante.fecha_publicacion.desc()).limit(3).all()

    return render_template('index.html', vacantes=vacantes)

@main_bp.route('/acerca')
def acerca():
     return render_template('acerca.html')
from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from ..models import Vacante
from datetime import datetime

vacante_bp = Blueprint('vacante', __name__)

@vacante_bp.route('/detalle/<int:id>')
def detalle(id):
    vacante = Vacante.query.get_or_404(id)
    return render_template('detalle.html', vacante=vacante)
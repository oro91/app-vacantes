from flask import Flask
from .models import db, Usuario
import os
from .routes.main_routes import main_bp

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'..', 'base_vacantes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        if not Usuario.query.filter_by(username='admin').first():
            admin = Usuario(
                username='admin',
                email='admin@gmail.com',
                password='admin123',
                estatus='Activo'
            )
            db.session.add(admin)
            db.session.commit()

    app.register_blueprint(main_bp)
    return app

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    POSTGRES = {
    'user': 'adrian',
    'pw': 'miniblog',
    'db': 'miblog',
    'host': 'localhost',
    'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

    # Registro de los Blueprints
    from .login import login_bp
    app.register_blueprint(login_bp)

    return app

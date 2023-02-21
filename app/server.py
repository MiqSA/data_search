from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api as api_blueprint
from main import main as main_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # db.init_app(app)

    app.register_blueprint(main_blueprint, url_prefix='')
    app.register_blueprint(api_blueprint, url_prefix='/v1.0')
    return app

server = create_app()

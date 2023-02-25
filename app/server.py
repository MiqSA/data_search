from flask import Flask
from sql_alchemy import db
from settings import config, DOC_SETTINGS


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    app.config.update(DOC_SETTINGS)

    from flask_apispec.extension import FlaskApiSpec
    from api import api as api_blueprint
    from api.views import get_info, get_info_by_date, get_info_by_title, get_info_by_uri
    from main import main as main_blueprint
    from main.views import upload, upload_informations

    docs = FlaskApiSpec(app)

    app.register_blueprint(main_blueprint, url_prefix='')
    app.register_blueprint(api_blueprint, url_prefix='/v1.0')

    docs.register(upload, blueprint='main')
    docs.register(upload_informations, blueprint='main')
    docs.register(get_info, blueprint='api')
    docs.register(get_info_by_date, blueprint='api')
    docs.register(get_info_by_title, blueprint='api')
    docs.register(get_info_by_uri, blueprint='api')

    db.init_app(app)
    return app


server = create_app('test')

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=8000)

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+mysqldb://root:v25xhycLlRY3sV7Z@database:3306/exercise'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:v25xhycLlRY3sV7Z@test-database:3306/test_exercise'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI ='mysql+mysqldb://root:v25xhycLlRY3sV7Z@database:3306/exercise'



config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}

VERSION = 'v1.0'

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

DOC_SETTINGS = {
    'APISPEC_SPEC': APISpec(
        title='API - Data Search',
        version=VERSION,
        plugins=[MarshmallowPlugin()],
        openapi_version='3.0.0',
    ),
    'APISPEC_SWAGGER_URL': '/docs/json', 
    'APISPEC_SWAGGER_UI_URL': '/docs/'
    }
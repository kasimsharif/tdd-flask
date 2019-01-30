import os
from flask_restful import Api

# local import
from instance.config import app_config
from app.models import db

from flask_api import FlaskAPI

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


config_name = os.getenv('ENVIRONMENT','testing')
app = create_app(config_name)

api = Api(app)

from service_apis.choice_list import ChoiceListAPI

api.add_resource(ChoiceListAPI, '/choicelists/', '/choicelists/<int:id>/')

if __name__ == '__main__':
    app.run()
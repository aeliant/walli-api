"""Controller package entry point, defining the global blueprint."""
from flask_restplus import Api
from flask import Blueprint
from ..config import API_VERSION

from .about_controller import api as about_api
from .tables_controller import api as table_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Walli API',
          version=API_VERSION,
          description='An api for managing your linux firewall (iptables)',
          prefix='/api')

api.add_namespace(about_api, path='/about')
api.add_namespace(table_api, path='/tables')

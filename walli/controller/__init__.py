"""Controller package entry point, defining the global blueprint."""
from flask_restplus import Api
from flask import Blueprint
from ..config import API_VERSION

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Walli API',
          version=API_VERSION,
          description='An api for managing Nginx configuration')

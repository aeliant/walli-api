"""Data Transfert Objects definitions."""
from flask_restplus import Namespace, fields


class AboutDto:
    api = Namespace('about', description='About related operation')
    about = api.model('about', {
        'version': fields.String(description='The api version.')
    })

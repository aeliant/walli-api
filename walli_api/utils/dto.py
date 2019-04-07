"""Data Transfert Objects definitions."""
from flask_restplus import Namespace, fields


class AboutDto:
    """About endpoint data transfert object for marshalling."""

    api = Namespace('about', description='About related operation')
    about = api.model('about', {
        'version': fields.String(description='The api version.')
    })


class TableDto:
    """Table endpoint data transfert objects for marshalling and documenting."""

    api = Namespace('table', description='Table related operation')


class ChainDto:
    """Chain data transfert object for marshalling and documenting."""

    api = Namespace('chain', description='Chain related operation')

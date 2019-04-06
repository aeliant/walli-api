"""Controller for table endpoints."""
from flask import request
from flask_restplus import Resource

from ..utils.dto import TableDto


api = TableDto.api

@api.route('')
class TableCollection(Resource):
    """Table collection endpoint."""

    @api.doc('GET_tables')
    def get(self):
        """List all registred tables."""
        

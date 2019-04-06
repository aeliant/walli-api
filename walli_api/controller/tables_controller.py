"""Controller for table endpoints."""
from flask import request
from flask_restplus import Resource

from ..utils.dto import TableDto
from ..service.table_service import fetch


api = TableDto.api

@api.route('')
class TableCollection(Resource):
    """Table collection endpoint."""

    @api.doc('GET_tables')
    @api.response(200, 'Tables successfully retrieved.')
    @api.response(400, 'A problem occured while retrieving tables.')
    def get(self):
        """List all registred tables."""
        return fetch()

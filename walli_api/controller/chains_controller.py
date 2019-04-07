"""Controller for chains endpoints."""
from flask import request
from flask_restplus import Resource

from ..utils.dto import ChainDto
from ..utils.exceptions import TableNotFoundException
from ..service.chain_service import fetch


api = ChainDto.api


@api.route('/<string:table_name>')
@api.param('table_name', 'The table name for which we want to retrieve chains')
class ChainCollection(Resource):
    """Chain collection endpoints."""

    @api.doc('GET_chains')
    @api.response(200, 'Chain collection successfully retrieved')
    @api.response(404, 'The given table does not exists.')
    def get(self, table_name):
        """List all registred chains for the given table."""
        try:
            return fetch(table_name)
        except TableNotFoundException as e:
            api.abort(code=404, message=str(e))

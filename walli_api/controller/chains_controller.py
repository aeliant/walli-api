"""Controller for chains endpoints."""
from flask import request
from flask_restplus import Resource

from ..utils.dto import ChainDto
from ..utils.exceptions import TableNotFoundException
from ..service.chain_service import fetch, list


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
            return list(table_name)
        except TableNotFoundException as e:
            api.abort(code=404, message=str(e))

@api.route('/<string:table_name>/<string:chain_name>')
@api.param('table_name', 'The table name for which we want to retrieve chains')
@api.param('chain_name', 'The chain name for which we want information')
class ChainItem(Resource):
    """Chain item endpoints."""

    @api.doc('GET_chains-name')
    @api.response(200, 'Chain successfully retrieved')
    @api.response(404, 'The chain or table does not exists')
    def get(self, table_name, chain_name):
        """Return information about the specified chain."""
        try:
            return fetch(table_name, chain_name.upper())
        except TableNotFoundException as e:
            api.abort(code=404, message=str(e))
        except ChainNotFoundException as e:
            api.abort(code=404, message=str(e))

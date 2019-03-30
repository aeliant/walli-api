"""Controller for api information"""
from flask import request
from flask_restplus import Resource

from ..utils.dto import AboutDto
from ..config import API_VERSION


api = AboutDto.api
_about = AboutDto.about


@api.route('')
class About(Resource):
    """Api information endpoint."""

    def get(self):
        """Check the API public information."""
        return dict(
            version=API_VERSION
        )

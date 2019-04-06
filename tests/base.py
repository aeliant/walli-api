"""Base class for flask testing."""
from flask_testing import TestCase
from app import app


class BaseTestCase(TestCase):
    """Base tests."""

    def create_app(self):
        """Create the flask testing application."""
        app.config.from_object('walli_api.config.TestingConfig')
        return app

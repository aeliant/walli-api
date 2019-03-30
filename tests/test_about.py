"""About controller functional tests."""
from base import BaseTestCase
from walli.config import API_VERSION


class TestAbout(BaseTestCase):
    """Functional tests for the about endpoints."""

    def test_endpoint_validity(self):
        """Checks the validity of the returned data from /api/about."""
        response = self.client.get('/api/about')

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json, dict)
        self.assertIn('version', response.json)
        self.assertEqual(API_VERSION, response.json['version'])

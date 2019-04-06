"""Tables controller functionnal tests."""
from base import BaseTestCase
from unittest.mock import patch


class TestTables(BaseTestCase):
    """Functional tests for the tables endpoint."""

    @patch('iptc.Table.ALL', ['Table1', 'Table2'])
    def test_table_collection(self):
        """Checks validity of the table collection."""
        response = self.client.get('/api/tables')

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json, list)
        self.assertEqual(2, len(response.json))
        self.assertEqual({'Table1', 'Table2'}, set(response.json))

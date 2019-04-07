"""Functionnal tests for the tables endpoint."""
from config import URL

import requests
import pytest


@pytest.mark.all_table
def test_tables_collection():
    """Checks validity of the tables collection."""
    response = requests.get('%s/tables' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), list)
    assert 5 == len(response.json())
    assert {
        'filter',
        'nat',
        'mangle',
        'raw',
        'nat',
        'security'
    } == set(response.json())

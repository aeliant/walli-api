"""Functionnal tests for the about endpoint."""
from config import URL
import requests

def test_about_validity():
    """Check validity of the returned result of /api/about."""
    response = requests.get('%s/about' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), dict)
    assert 'version' in response.json()

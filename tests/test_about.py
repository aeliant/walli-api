"""Functionnal tests for the about endpoint."""
from os import environ

import requests

HOST = environ.get('DOCKER_TESTING_HOST', 'localhost')
PORT = environ.get('DOCKER_TESTING_PORT', '54310')
URL = 'http://%s:%s/api' % (HOST, PORT)

def test_about_validity():
    """Check validity of the returned result of /api/about."""
    response = requests.get('%s/about' % URL)

    assert 200 == response.status_code
    assert isinstance(response.json(), dict)
    assert 'version' in response.json()

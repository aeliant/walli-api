"""Testing configurations."""
import os

HOST = os.environ.get('DOCKER_TESTING_HOST', 'localhost')
PORT = os.environ.get('DOCKER_TESTING_PORT', '54310')
URL = 'http://%s:%s/api' % (HOST, PORT)

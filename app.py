"""Walli application entry point."""
import os
from walli_api import create_app
from walli_api.controller import blueprint

app = create_app(os.getenv('FLASK_ENV', 'dev'))
app.register_blueprint(blueprint)

app.app_context().push()

def run():
    app.run()

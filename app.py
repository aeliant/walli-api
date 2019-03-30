"""Walli application entry point."""
import os
from walli import create_app
from walli.controller import blueprint

app = create_app(os.getenv('FLASK_ENV', 'dev'))
app.register_blueprint(blueprint)

app.app_context().push()

"""Walli application entry point."""
import os
from walli import create_app

app = create_app(os.getenv('FLASK_ENV', 'dev'))
app.app_context().push()

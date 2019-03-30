"""Flask configuration file."""
import os

API_VERSION = '0.0.1'

class Config:
    """Base configuration for all 3 environments."""

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'secret-to-change')
    DEBUG = False

class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""

    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    tests=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

class BaseConfig(object):
    """Base config class"""
    SECRET_KEY = 'Password123'
    DEBUG = True
    TESTING = False


class ProductionConfig(object):
    """Production specific config"""
    DEBUG = False
    SECRET_KEY = 'Password123'


class StagingConfig(object):
    """Staging specific config"""
    DEBUG = True


class DevelopmentConfig(object):
    """Development environment specific config"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another random secret key'


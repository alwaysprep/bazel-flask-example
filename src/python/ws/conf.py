class BaseConfig(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    ENV = 'production'


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

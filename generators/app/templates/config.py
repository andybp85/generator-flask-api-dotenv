import os, tempfile


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
<% if (databaseMapper === 'sqlalchemy') { -%>
    SQLALCHEMY_DATABASE_URI = os.environ.get('<%= appEnvVar %>_PRODUCTION_DATABASE_URI')
<% } else { -%>
    pass
<% } -%>


class DevelopmentConfig(Config):
    DEBUG = True
<% if (databaseMapper === 'sqlalchemy') { -%>
    SQLALCHEMY_DATABASE_URI = os.environ.get('<%= appEnvVar %>_DEVELOPMENT_DATABASE_URI')
<% } -%>


class TestingConfig(Config):
    TESTING = True
<% if (databaseMapper === 'sqlalchemy') { -%>
    db_file = tempfile.NamedTemporaryFile()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True
<% } -%>


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}

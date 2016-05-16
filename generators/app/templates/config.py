import os, tempfile
from flask.ext.dotenv import DotEnv


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(self, app):
        env = DotEnv()
        env.init_app(app, verbose_mode=True)

<% if (databaseMapper === 'sqlalchemy') { -%>
        if self.__name__ != 'TestingConfig':
            prefix = self.__name__.replace('Config', '').upper()
            env.alias(maps={
                '<%= appEnvVar %>_' + prefix + '_DATABASE_URI': 'SQLALCHEMY_DATABASE_URI'
            })
<% } -%>



class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


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
    'default': ProductionConfig,
}

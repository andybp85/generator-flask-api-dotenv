#! ../env/bin/python
# -*- coding: utf-8 -*-
from <%= appName %> import create_app



class TestConfig:
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app(os.getenv('<%= appEnvVar %>_CONFIG', 'development'))

        assert app.config['DEBUG'] is True
        <% if (databaseMapper === 'sqlalchemy') { -%>
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('<%= appEnvVar %>_DEVELOPMENT_DATABASE_URI')
        <% } -%>

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app(os.getenv('<%= appEnvVar %>_CONFIG', 'testing'))

        assert app.config['TESTING'] is True
        <% if (databaseMapper === 'sqlalchemy') { -%>
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('<%= appEnvVar %>_TESTING_DATABASE_URI')
        <% } -%>

    def test_prod_config(self):
        """ Tests if the production config loads correctly """

        app = create_app(os.getenv('<%= appEnvVar %>_CONFIG', 'production'))

        assert app.config['DEBUG'] is False
        assert app.config['TESTING'] is False
        <% if (databaseMapper === 'sqlalchemy') { -%>
        assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('<%= appEnvVar %>_PRODUCTION_DATABASE_URI')
        <% } -%>

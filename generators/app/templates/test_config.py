#! ../env/bin/python
# -*- coding: utf-8 -*-
from <%= appName %> import create_app



class TestConfig:
    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app('development')

        assert app.config['DEBUG'] is True
<% if (databaseMapper === 'sqlalchemy') { -%>
        assert app.config['SQLALCHEMY_DATABASE_URI']
<% } -%>

    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app('testing')

        assert app.config['TESTING'] is True

    def test_prod_config(self):
        """ Tests if the production config loads correctly """

        app = create_app('production')

        assert app.config['DEBUG'] is False
        assert app.config['TESTING'] is False
<% if (databaseMapper === 'sqlalchemy') { -%>
        assert app.config['SQLALCHEMY_DATABASE_URI'] or app.config['SQLALCHEMY_DATABASE_URI'] == ""
<% } -%>

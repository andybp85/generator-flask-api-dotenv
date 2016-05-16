#! /usr/bin/env python

import os

from flask.ext.script import Manager
from flask.ext.script.commands import ShowUrls, Clean

from <%= appName %> import create_app<% if (databaseMapper === 'sqlalchemy') { -%>, db<% } %>


app = create_app(os.getenv('<%= appEnvVar %>_CONFIG', 'default'))

manager = Manager(app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """
    return dict(app=app<% if (databaseMapper === 'sqlalchemy') { -%>, db=db<% } %>)

<% if (databaseMapper === 'sqlalchemy') { -%>
@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """
    db.create_all()
<% } -%>

@manager.command
def test():
    """ run all your tests using py.test
    """
    from flake8.engine import get_style_guide
    import pytest

    pytest.main("-x tests")


if __name__ == '__main__':
    manager.run()

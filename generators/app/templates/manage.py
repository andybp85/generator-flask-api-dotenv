#! /usr/bin/env python
from flask.ext.script import Manager
from flask.ext.script.commands import ShowUrls, Clean

from <%= appName %> import create_app<% if (databaseMapper === 'sqlalchemy') { -%>, db<% } %>


app = create_app("development")

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
    """ flake8 and run all your tests using py.test
    """
    import pytest

    pytest.main("--cov=<%= appName %> --mccabe --flakes tests")


if __name__ == '__main__':
    manager.run()

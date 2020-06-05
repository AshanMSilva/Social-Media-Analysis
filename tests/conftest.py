import pytest
from social_media_analysis import create_app, db
from social_media_analysis.models import User
from social_media_analysis.test_config import TestConfig

@pytest.fixture(scope='module')
def new_user():
    user = User('ashan','patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data      
    user1 = User(username='ashan', email='patkennedy79@gmail.com', password='FlaskIsAwesome')
    user2 = User(username='silva', email='kennedyfamilyrecipes@gmail.com', password='PaSsWoRd')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()

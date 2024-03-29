import os

class TestConfig:
# Get the folder of the top-level directory of this project
	BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
	SECRET_KEY = 'bad_secret_key'
	DEBUG = True

# SQLAlchemy
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app_test.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
	BCRYPT_LOG_ROUNDS = 4

# Enable the TESTING flag to disable the error catching during request handling
# so that you get better error reports when performing test requests against the application.
	TESTING = True

# Disable CSRF tokens in the Forms (only valid for testing purposes!)
	WTF_CSRF_ENABLED = False

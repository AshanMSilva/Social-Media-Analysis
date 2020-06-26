import pytest
import flask  
from flask import request
from social_media_analysis import create_app, db
from social_media_analysis.models import User
from social_media_analysis.test_config import TestConfig
from social_media_analysis.codes.FacebookCodes.bot_detection import BotAccountDetection
from social_media_analysis.codes.FacebookCodes.ad_clicks_prediction import AdPrediction,AdImpressionPrediction,BestSolutions
# from social_media_analysis.facebook.routes import 
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=TestConfig)
    import os 
    SECRET_KEY = os.urandom(32)
    flask_app.config['SECRET_KEY'] = SECRET_KEY

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


# def test_bot_account():
#     botdetection=BotAccountDetection()
#     a=botdetection.get_info('https://www.facebook.com/sanduniayeshika.silva')
#     real={'Address': 'Edman mawatha handiya, Eluwila, Panadura.', 'Birthday': 'July 13, 1992', 'Gender': 'Female', 'Interested In': 'Men and Women', 'Religious Views': 'Buddhist', 'Education': ['Faculty of Medicine, University of Jaffna', 'Sri Sumangala Girls School', 'Sri Sumangala Girls School Panadura'], 'Family Members': [2, ['Chinthaka Udara', 'Kaveesha Silva']], 'tagged_photo_count': 1}
#     # print (a)
#     assert a==real

def test_facebook_bot(test_client):

    response=test_client.post('/facebook/bot', data=dict(link='https://www.facebook.com/sisara.kahatapitiya.9'))

    assert response.status_code == 200

# def test_facebook_bot(test_client):

#     response=test_client.post('/bot')
#     assert response.status_code == 200 

# def test_face(test_client):
#     app = flask.Flask(__name__)
#     with app.test_client() as c:
#         rv = c.get('/?tequila=42')
#         assert request.args['tequila'] == '42'
# def test_nnn(test_client):
#     app = flask.Flask(__name__)
#     with app.test_client() as c:
#         rv = c.post('/facebook', json={ 'link': 'https://www.facebook.com/sisara.kahatapitiya.9' })
#         assert request.args['link'] == 'https://www.facebook.com/sisara.kahatapitiya.9'


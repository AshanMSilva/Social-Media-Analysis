import os


class Config:
    SECRET_KEY = '1234567890'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/social_media_analysis'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'smanalysis.uom@gmail.com'
    MAIL_PASSWORD = 'Smanalysis@123'
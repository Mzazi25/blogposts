import  os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:Mzazi25@localhost/blog'
    QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

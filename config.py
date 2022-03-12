import  os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:Mzazi25@localhost/blog'
    BLOG_API_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:Mzazi25@localhost/blog'

    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    liked = db.relationship('Comment', foreign_keys='Comment.users_id', backref='users',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Blog(db.Model):
    __tablename__= "blogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String(100), unique=True,nullable=False)
    message = db.Column(db.String(), unique=True,nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    likes = db.relationship('Comment', backref='blogs', lazy='dynamic')
    
class Comment(db.Model):
    __tablename__= 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id') )
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id') )
    comment = db.Column(db.String(), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)

class Quotes:
    '''
    class defines quotes objects
    '''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
    

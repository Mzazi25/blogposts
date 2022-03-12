from flask import render_template,request,redirect,url_for,abort
from .import main
from ..requests import get_random_quotes
from flask_login import login_required, current_user
from ..models import User,Comment,Blog
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos, login_manager

# creating an auth instance
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

login_manager.login_view = 'main.login'


#views
@main.route('/')
def index():
    '''
    view root page function that returns indext.html and its data
    '''
    quotes = get_random_quotes()
    print(quotes)
    likes = Comment.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data,users_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    blog = Blog.query.all()
    user = User.query.all()
    return render_template('index.html',likes=likes,quotes=quotes, user=user,form=form,blog=blog)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    # fetch data
    blog = Blog.query.all()

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        message = form.message.data

        new_blog = Blog(title=title, message=message,user_id=current_user.id)

        # add data to db
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('profile/profile.html',form=form,name=current_user.username, blog=blog)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

from flask import render_template,request,redirect,url_for,abort
from .import main
# from ..requests import Quot
from flask_login import login_required, current_user
from ..models import User,Comment,Blog
from .forms import UpdateProfile
from .. import db,photos

@main.route('/main/<id>', methods=['GET', 'POST'])
def fail(id):
    likes = Comment.query.all()
    blog = Blog.query.filter_by(id=id).first()
    user = User.query.filter_by(id=blog.user_id).first()
    
    return render_template('index.html',user=user,blog=blog, likes=likes)


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



# Views
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


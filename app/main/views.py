from flask import render_template,request,redirect,url_for,abort
from .import main
# from ..requests import 
from flask_login import login_required, current_user
from ..models import User
from .forms import UpdateProfile
from .. import db,photos

# @main.route('/',methods=[ 'POST','GET'])
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''

#     data = {
#         "title":"News API",
#         "heading": "News"
#     }
#     sources = get_news()
#     articles= get_articles('creative')
    
    
#     return render_template('index.html',context=data,sources = sources,article=articles)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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


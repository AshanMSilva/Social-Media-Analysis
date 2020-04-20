from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from social_media_analysis import db
from social_media_analysis.models import Post, Comment
from social_media_analysis.posts.forms import PostForm
from social_media_analysis.users.forms import RegistrationForm, LoginForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new")
@login_required
def new_post():
    try:
        title = request.args.get('title')
        content = request.args.get('content')
        if(title==None or content==None):
            flash('title and content cannot be null','warning')
            return redirect(url_for('main.forum'))
        else:
            post = Post(title=title, content=content, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('main.forum'))        
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))


@posts.route("/post/<int:post_id>")
def post(post_id):
    try:
        loginmodalshow='close'
        loginform = LoginForm()
        if(loginform.validate_on_submit()==False and loginform.login.data):
            loginmodalshow='loginformmodal'
        if loginform.validate_on_submit() and loginform.login.data:
            remember=loginform.remember.data
            email=loginform.email.data
            password=loginform.password.data
            return redirect(url_for('users.login', remember=remember, email=email, password=password))
        modalshow='close'
        registerform = RegistrationForm()
        if(registerform.validate_on_submit()==False and registerform.signup.data):
            modalshow='registerformmodal'
        if registerform.validate_on_submit() and registerform.signup.data:
            username=registerform.username.data
            email=registerform.email.data
            password=registerform.password.data
            return redirect(url_for('users.register', username=username, email=email, password=password))
        post = Post.query.get_or_404(post_id)
        comments = post.comments
        print(comments)
        return render_template('post.html', title=post.title, post=post, comments=comments, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    try:
        loginmodalshow='close'
        loginform = LoginForm()
        if(loginform.validate_on_submit()==False and loginform.login.data):
            loginmodalshow='loginformmodal'
        if loginform.validate_on_submit() and loginform.login.data:
            remember=loginform.remember.data
            email=loginform.email.data
            password=loginform.password.data
            return redirect(url_for('users.login', remember=remember, email=email, password=password))
        modalshow='close'
        registerform = RegistrationForm()
        if(registerform.validate_on_submit()==False and registerform.signup.data):
            modalshow='registerformmodal'
        if registerform.validate_on_submit() and registerform.signup.data:
            username=registerform.username.data
            email=registerform.email.data
            password=registerform.password.data
            return redirect(url_for('users.register', username=username, email=email, password=password))
        post = Post.query.get_or_404(post_id)
        if post.author != current_user:
            abort(403)
        form = PostForm()
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            db.session.commit()
            flash('Your post has been updated!', 'success')
            return redirect(url_for('posts.post', post_id=post.id))
        elif request.method == 'GET':
            form.title.data = post.title
            form.content.data = post.content
        return render_template('create_post.html', title='Update Post',
                               form=form, legend='Update Post', registerform=registerform, modalshow=modalshow,loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        if post.author != current_user:
            abort(403)
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
        return redirect(url_for('main.forum'))
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

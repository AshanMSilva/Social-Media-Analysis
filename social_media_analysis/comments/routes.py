from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from social_media_analysis import db
from social_media_analysis.models import Comment, Post
from social_media_analysis.comments.forms import CommentForm
from social_media_analysis.users.forms import RegistrationForm, LoginForm

comments = Blueprint('comments', __name__)


@comments.route("/post/<int:post_id>/comment/new", methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
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
        form = CommentForm()
        if form.validate_on_submit():
        	post = Post.query.get_or_404(post_id)
        	comment = Comment(content=form.content.data, post=post, comment_author=current_user)
        	db.session.add(comment)
        	db.session.commit()
        	flash('Your comment has been added!', 'success')
        	return redirect(url_for('main.home'))
        return render_template('create_comment.html', title='New Comment', form=form, Legend='New Comment', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

@comments.route("/comment/<int:comment_id>")
def comment(comment_id):
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
        comment = Comment.query.get_or_404(comment_id)
        return render_template('comment.html', comment_author=comment.comment_author, comment=comment, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

@comments.route("/post/<int:post_id>/comment/<int:comment_id>/update", methods=['GET', 'POST'])
@login_required
def update_comment(comment_id, post_id):
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
        comment = Comment.query.get_or_404(comment_id)
        if comment.comment_author != current_user:
            abort(403)
        form = CommentForm()
        if form.validate_on_submit():
            comment.content = form.content.data
            db.session.commit()
            flash('Your comment has been updated!', 'success')
            return redirect(url_for('posts.post', post_id=post_id))
        elif request.method == 'GET':
            form.content.data = comment.content
        return render_template('create_comment.html', title='Update Comment',
                               form=form, legend='Update Comment', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))

@comments.route("/post/<int:post_id>/comment/<int:comment_id>/delete", methods=['POST'])
@login_required
def delete_comment(comment_id, post_id):
    try:
        comment = Comment.query.get_or_404(comment_id)
        if comment.comment_author != current_user:
            abort(403)
        db.session.delete(comment)
        db.session.commit()
        flash('Your comment has been deleted!', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.forum'))
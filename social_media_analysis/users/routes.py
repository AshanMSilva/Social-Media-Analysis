from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from social_media_analysis import db, bcrypt
from social_media_analysis.models import User, Post, Comment
from social_media_analysis.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from social_media_analysis.users.utils import save_picture, send_reset_email
from social_media_analysis.users.forms import RegistrationForm

users = Blueprint('users', __name__)


@users.route("/register")
def register():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        if(username==None or email==None or password==None):
            flash('username and email cannot be null','warning')
            return redirect(url_for('main.home'))
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.home'))
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))

@users.route("/login")
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        remember = request.args.get('remember')
        email = request.args.get('email')
        password = request.args.get('password')
        if(remember==None or email==None or password==None):
            flash('password and email cannot be null','warning')
            return redirect(url_for('main.home'))
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            flash('Login Successful. Welcome to our Social Media Analysis Website', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for('main.home'))
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))

@users.route("/logout")
def logout():
    try:
        logout_user()
        return redirect(url_for('main.home'))
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
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
        form = UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('users.account'))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.email.data = current_user.email
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        return render_template('account.html', title='Account',
                               image_file=image_file, form=form, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))

@users.route("/user/<string:username>/posts")
def user_posts(username):
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
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=username).first_or_404()
        posts = Post.query.filter_by(author=user)\
            .order_by(Post.date_posted.desc())\
            .paginate(page=page, per_page=5)
        return render_template('user_posts.html', posts=posts, user=user, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))
@users.route("/user/<string:username>/comments")
def user_comments(username):
    try:
        loginmodalshow='close'
        loginform = LoginForm()
        if(loginform.validate_on_submit()==False and loginform.login.data):
            loginmodalshow='loginformmodal'
        modalshow='close'
        registerform = RegistrationForm()
        if(registerform.validate_on_submit()==False and registerform.signup.data):
            modalshow='show'
        if registerform.validate_on_submit() and registerform.signup.data:
            username=registerform.username.data
            email=registerform.email.data
            password=registerform.password.data
            return redirect(url_for('users.register', username=username, email=email, password=password))
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=username).first_or_404()
        comments = Comment.query.filter_by(comment_author=user)\
            .order_by(Comment.date_posted.desc())\
            .paginate(page=page, per_page=5)
        return render_template('user_comments.html', comments=comments, user=user, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))
@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
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
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            send_reset_email(user)
            flash('An email has been sent with instructions to reset your password.', 'info')
            return redirect(url_for('main.home'))
        return render_template('reset_request.html', title='Reset Password', form=form, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
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
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        user = User.verify_reset_token(token)
        if user is None:
            flash('That is an invalid or expired token', 'warning')
            return redirect(url_for('users.reset_request'))
        form = ResetPasswordForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated! You are now able to log in', 'success')
            return redirect(url_for('main.home'))
        return render_template('reset_token.html', title='Reset Password', form=form, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.home'))
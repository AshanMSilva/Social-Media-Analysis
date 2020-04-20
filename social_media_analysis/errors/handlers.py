from flask import Blueprint, render_template
from social_media_analysis.users.forms import RegistrationForm, LoginForm

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
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
	return render_template('errors/404.html', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow), 404

@errors.app_errorhandler(403)
def error_403(error):
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
	return render_template('errors/403.html', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow), 403


@errors.app_errorhandler(500)
def error_500(error):
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
	return render_template('errors/500.html',registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow), 500

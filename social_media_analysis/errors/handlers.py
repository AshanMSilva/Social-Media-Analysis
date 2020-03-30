from flask import Blueprint, render_template
from social_media_analysis.users.forms import RegistrationForm

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('errors/404.html', registerform=registerform, modalshow=modalshow), 404

@errors.app_errorhandler(403)
def error_403(error):
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('errors/403.html', registerform=registerform, modalshow=modalshow), 403


@errors.app_errorhandler(500)
def error_500(error):
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('errors/500.html',registerform=registerform, modalshow=modalshow), 500

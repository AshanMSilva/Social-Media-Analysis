from flask import render_template, request, Blueprint, redirect, url_for
from social_media_analysis.models import Post
from social_media_analysis.twitter.forms import NameForm, BotForm,HashtagForm
from social_media_analysis.posts.forms import PostForm
from social_media_analysis.users.forms import RegistrationForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('home.html', registerform=registerform, modalshow=modalshow)


@main.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')

@main.route("/twitter", methods=['GET', 'POST'])
def twitter():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	botform = BotForm()
	if botform.validate_on_submit() and botform.submit.data:
		bot_account_name = botform.name.data
		return redirect(url_for('twitter.bot_account_detection', name=bot_account_name))

	hashtagform = HashtagForm()
	if hashtagform.validate_on_submit() and hashtagform.hashtagsubmit.data:
		hashtag = hashtagform.hashtag.data
		return redirect(url_for('twitter.hashtag_tweets', hashtag=hashtag))

	screennameform = NameForm()
	if screennameform.validate_on_submit() and screennameform.search.data:
		screen_name = screennameform.name.data
		return redirect(url_for('twitter.user_details', name=screen_name))
	return render_template('twitter.html', title='Twitter', screennameform=screennameform, botform=botform, hashtagform=hashtagform, registerform=registerform, modalshow=modalshow)

@main.route("/facebook", methods=['GET', 'POST'])
def facebook():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('facebook.html', title='Facebook', registerform=registerform, modalshow=modalshow)

@main.route("/youtube", methods=['GET', 'POST'])
def youtube():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('youtube.html', title='Youtube', registerform=registerform, modalshow=modalshow)

@main.route("/stack_overflow", methods=['GET', 'POST'])
def stack_overflow():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	return render_template('stack_overflow.html', title='Stack Overflow', registerform=registerform)

@main.route("/forum", methods=['GET', 'POST'])
def forum():
	modalshow='close'
	registerform = RegistrationForm()
	if(registerform.validate_on_submit()==False and registerform.signup.data):
		modalshow='show'
	if registerform.validate_on_submit() and registerform.signup.data:
		username=registerform.username.data
		email=registerform.email.data
		password=registerform.password.data
		return redirect(url_for('users.register', username=username, email=email, password=password))
	form = PostForm()
	if form.validate_on_submit():
		return redirect(url_for('posts.new_post', title=form.title.data, content=form.content.data))
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('forum.html', posts=posts, form=form, registerform=registerform, modalshow=modalshow)

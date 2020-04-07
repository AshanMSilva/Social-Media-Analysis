from flask import render_template, request, Blueprint, redirect, url_for
from social_media_analysis.models import Post
from social_media_analysis.twitter.forms import NameForm, BotForm,HashtagForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/twitter", methods=['GET', 'POST'])
def twitter():
	botform = BotForm()
	if botform.validate_on_submit() and botform.submit.data:
		bot_account_name = botform.name.data
		return redirect(url_for('twitter.bot_account_detection', name=bot_account_name))

	hashtagform = HashtagForm()
	if hashtagform.validate_on_submit() and hashtagform.hashtagsubmit.data:
		hashtag = hashtagform.hashtag.data
		return redirect(url_for('twitter.hashtag_tweets()', hashtag=hashtag))

	screennameform = NameForm()
	if screennameform.validate_on_submit() and screennameform.search.data:
		screen_name = screennameform.name.data
		return redirect(url_for('twitter.user_details', name=screen_name))
	return render_template('twitter.html', title='Twitter', screennameform=screennameform, botform=botform)

@main.route("/facebook")
def facebook():
	return render_template('facebook.html', title='Facebook')

@main.route("/youtube")
def youtube():
	return render_template('youtube.html', title='Youtube')

@main.route("/stack_overflow")
def stack_overflow():
	return render_template('stack_overflow.html', title='Stack Overflow')

from flask import render_template, request, Blueprint, redirect, url_for
from social_media_analysis.models import Post
from social_media_analysis.twitter.forms import screenNameForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/twitter", methods=['GET', 'POST'])
def twitter():
	nameform = screenNameForm()
	if nameform.validate_on_submit():
		name = nameform.name.data
		return redirect(url_for('twitter.user_details', name=name))
	return render_template('twitter.html', title='Twitter', form=nameform)

@main.route("/facebook")
def facebook():
	return render_template('facebook.html', title='Facebook')

@main.route("/youtube")
def youtube():
	return render_template('youtube.html', title='Youtube')

@main.route("/stack_overflow")
def stack_overflow():
	return render_template('stack_overflow.html', title='Stack Overflow')

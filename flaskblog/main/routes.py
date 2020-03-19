from flask import render_template, request, Blueprint
from flaskblog.models import Post

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

@main.route("/twitter")
def twitter():
	return render_template('twitter.html', title='Twitter')

@main.route("/facebook")
def facebook():
	return render_template('facebook.html', title='Facebook')

@main.route("/youtube")
def youtube():
	return render_template('youtube.html', title='Youtube')

@main.route("/stack_overflow")
def stack_overflow():
	return render_template('stack_overflow.html', title='Stack Overflow')

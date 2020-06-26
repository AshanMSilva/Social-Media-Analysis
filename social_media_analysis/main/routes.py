from flask import render_template, request, Blueprint, redirect, url_for,flash
from social_media_analysis.models import Post
from social_media_analysis.twitter.forms import NameForm, BotForm,HashtagForm, TweetForm
from social_media_analysis.youtube.forms import ChannelDetailForm,SentimentAnalysisForm,ViewPredictionForm,ViralVideoForm
from social_media_analysis.posts.forms import PostForm
from social_media_analysis.users.forms import RegistrationForm, LoginForm
from social_media_analysis.facebook.forms import AdForm,FbBotForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
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
        return render_template('home.html', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
    except:
        flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
        return redirect(url_for('main.home'))

@main.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')

@main.route("/twitter", methods=['GET', 'POST'])
def twitter():
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
		
        botform = BotForm()
        botmodal='close'
        if(botform.validate_on_submit()==False and botform.submit.data):
            botmodal='botdetectionmodel'
        if botform.validate_on_submit() and botform.submit.data:
            bot_account_name = botform.name.data
            return redirect(url_for('twitter.bot_account_detection', name=bot_account_name))

        hashtagform = HashtagForm()
        hashtagmodal='close'
        if(hashtagform.validate_on_submit()==False and hashtagform.hashtagsubmit.data):
            hashtagmodal='hashtagmodel'
        if hashtagform.validate_on_submit() and hashtagform.hashtagsubmit.data:
            hashtag = hashtagform.hashtag.data
            return redirect(url_for('twitter.hashtag_tweets', hashtag=hashtag))

        screennamemodal='close'
        screennameform = NameForm()
        if(screennameform.validate_on_submit()==False and screennameform.search.data):
            screennamemodal='searchforaccount'
        if screennameform.validate_on_submit() and screennameform.search.data:
            screen_name = screennameform.name.data
            return redirect(url_for('twitter.user_details', name=screen_name))
        
        predtweetmodal='close'
        tweetform = TweetForm()
        if(tweetform.validate_on_submit()==False and tweetform.likespredict.data):
            predtweetmodal='likespredmodal'
        if tweetform.validate_on_submit()and tweetform.likespredict.data:
            screen_name = tweetform.name.data
            tweet = tweetform.tweet.data
            time = tweetform.time.data
            return redirect(url_for('twitter.user_tweets', name=screen_name, tweet=tweet, time=time))

        return render_template('twitter.html', title='Twitter', tweetform=tweetform, screennameform=screennameform, botform=botform, hashtagform=hashtagform, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow, predtweetmodal=predtweetmodal, screennamemodal=screennamemodal, botmodal=botmodal, hashtagmodal=hashtagmodal)
    except:
        flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
        return redirect(url_for('main.home'))
@main.route("/facebook", methods=['GET', 'POST'])
def facebook():
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

	#### handle facebook advertisements
	adform = AdForm()
	adpredict_model='close'
	if(adform.validate_on_submit()==False and adform.submit.data):
		adpredict_model='adpredictmodel'
	if adform.validate_on_submit() and adform.submit.data:
		gender = adform.gender.data
		adText = adform.adText.data
		weekday = adform.weekday.data
		minAge = adform.minAge.data
		maxAge = adform.maxAge.data
		adSpends = adform.adSpends.data 
		return redirect(url_for('facebook.fbAdClicksPredict',gender=gender,adText=adText,weekday=weekday,minAge=minAge,maxAge=maxAge,adSpends=adSpends))

	### handle senetiments
	# sentiform=SentimentForm()
	# sentiment_model='close' 
	# if(sentiform.validate_on_submit()==False and sentiform.submit.data):
	# 	sentiment_model='sentimentmodel'
	# if sentiform.validate_on_submit() and sentiform.submit.data:
	# 	file_up = sentiform.upload
	# 	return redirect(url_for('facebook.sentiment',file_up=file_up))

	
	### handle bot detection
	botform=FbBotForm()
	botdetection_model='close'
	if(botform.validate_on_submit()==False and botform.submit.data):
		botdetection_model='botdetectionmodel'
	if botform.validate_on_submit() and botform.submit.data:
		link = botform.link.data
		return redirect(url_for('facebook.bot',link=link))


	return render_template('facebook.html', adform=adform,botform=botform, title='Facebook', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow,adpredict_model=adpredict_model)

@main.route("/youtube", methods=['GET', 'POST'])
def youtube():
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
        
        channeldetailmodal='close'
        channeldetailform = ChannelDetailForm()
        if(channeldetailform.validate_on_submit()==False and channeldetailform.search.data):
            channeldetailmodal='channeldetails'
        if channeldetailform.validate_on_submit() and channeldetailform.search.data:
            channel_id = channeldetailform.name.data
            return redirect(url_for('youtube.viewChannelDetails', name=channel_id))
             
        
        sentimentanalysismodal='close'
        sentimentanalysisform = SentimentAnalysisForm()
        if(sentimentanalysisform.validate_on_submit()==False and sentimentanalysisform.searchSent.data):
            sentimentanalysismodal='analysecomments'
        if sentimentanalysisform.validate_on_submit() and sentimentanalysisform.searchSent.data:
            video_id = sentimentanalysisform.name.data
            return redirect(url_for('youtube.analyseComments', name=video_id))
        
        viewpredictionmodal='close'
        viewpredictionform = ViewPredictionForm()
        if(viewpredictionform.validate_on_submit()==False and viewpredictionform.viewspredict.data):
            viewpredictionmodal='predictviews'
        if viewpredictionform.validate_on_submit() and viewpredictionform.viewspredict.data:
            channel_id = viewpredictionform.channel.data
            category_id = viewpredictionform.category.data
            dur = viewpredictionform.length.data
            return redirect(url_for('youtube.predictViews', name=channel_id,dur=dur,category_id=category_id))
      
        
        viralvideomodal = 'close'
        viralvideofrom=ViralVideoForm()
        if(viralvideofrom.validate_on_submit()==False):
            viralvideomodal='viralvideos'
        if viralvideofrom.validate_on_submit():
            return redirect(url_for('youtube.viralVideos'))
        
        
        return render_template('youtube.html', title='Youtube',viewpredictionform= viewpredictionform,viewpredictionmodal = viewpredictionmodal,
                               sentimentanalysisform=sentimentanalysisform, registerform=registerform, channeldetailform=channeldetailform,
                               sentimentanalysismodal=sentimentanalysismodal,channeldetailmodal = channeldetailmodal, modalshow=modalshow, loginform=loginform, 
                               loginmodalshow=loginmodalshow,viralvideomodal=viralvideomodal,viralvideofrom=viralvideofrom)
    except:
        flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
        return redirect(url_for('main.home'))

@main.route("/stack_overflow", methods=['GET', 'POST'])
def stack_overflow():
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
		return render_template('stack_overflow.html', title='Stack Overflow', registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
	except:
		flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
		return redirect(url_for('main.home'))

@main.route("/forum", methods=['GET', 'POST'])
def forum():
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
		form = PostForm()
		if form.validate_on_submit():
			return redirect(url_for('posts.new_post', title=form.title.data, content=form.content.data))
		page = request.args.get('page', 1, type=int)
		posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
		return render_template('forum.html', posts=posts, form=form, registerform=registerform, modalshow=modalshow, loginform=loginform, loginmodalshow=loginmodalshow)
	except:
		flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
		return redirect(url_for('main.home'))
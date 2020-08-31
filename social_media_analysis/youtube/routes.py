import pandas as pd
from datetime import date,datetime
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from social_media_analysis.users.forms import (RegistrationForm, LoginForm)
from social_media_analysis.youtube.codes.SubscriberCount import getChannelData
from social_media_analysis.youtube.codes.getcomments import getComments,sentimentAnalysis
from social_media_analysis.youtube.codes.videoData import getVideoDetails,getVideoCategory 


youtube = Blueprint('youtube', __name__)

@youtube.route("/youtube/viewchannel/<string:name>")
@login_required

def viewChannelDetails(name):
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
    
    try:
        Cid,vid,view,sub,name,description,Date,privacy,featured,colour,bannerurl,location,customurl,language = getChannelData(name)
    #colour = "#ffffff"
    except:
        flash("Couldn't get data. Please check whether entered details are correct","warning")
        return redirect(url_for('main.youtube'))
    
    viewratio = (round(view/vid))
    url = "https://www.youtube.com/channel/" + Cid   
    
    return render_template('viewchannel.html',customurl = customurl, location =location,viewratio=viewratio,Cid=Cid,featured=featured,colour=colour,
                           bannerurl=bannerurl, privacy=privacy,description = description, Date = Date, name= name,vid = vid, view = view, sub = sub, 
                           loginmodalshow= loginmodalshow, loginform = loginform, modalshow =modalshow, registerform=registerform, url=url, language=language )
        

@youtube.route("/youtube/commentanalysis/<string:name>")
@login_required

def analyseComments(name):
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
     
    negcom = 0
    poscom = 0
    neucom = 0
    exPosCom=[]
    exNegCom=[]
    exNeuCom=[]
    analysedCom=0
    
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            "👏🏽","👌", "♥️","👍","😍","😀","🔥","💪","✌️","😘","❤","😊"]
    
    comments, replyCount = getComments(name)
    topcom = len(comments)
    
    for comment in comments:
        for c in char:
            if c in comment:
                break
        else:
            print(comment)
            continue
        val = sentimentAnalysis(comment)
        analysedCom+=1
        if val==1:
            poscom+=1
            exPosCom.append(comment)
        elif val==-1 :
            negcom+=1
            exNegCom.append(comment)
        else:
            neucom+=1
            exNeuCom.append(comment)
        #print(comment,val)
    title,des,Date,channel,categoryID,language,duration,privacy,status,views,likes,dislikes = getVideoDetails(name)
    #des = des.replace("\n","<br/>")
    category = getVideoCategory(categoryID)
    url = "https://www.youtube.com/watch?v=" + name
    exPosCom=exPosCom[:4]
    exNegCom=exNegCom[:4]
    exNeuCom=exNeuCom[:4]
 
    return render_template('commentanalysis.html',analysedCom=analysedCom,exPosCom=exPosCom,exNegCom=exNegCom,exNeuCom=exNeuCom,name=name,topcom=topcom, 
                           neucom = neucom, negcom=negcom,poscom=poscom, replyCount=replyCount,likes=likes, loginmodalshow= loginmodalshow, 
                           loginform = loginform,categoryID=categoryID,language=language,duration=duration,privacy=privacy,status=status,category=category,
                           title=title,des=des,Date=Date,channel=channel,modalshow =modalshow, registerform=registerform,views=views,dislikes=dislikes, url=url)


@youtube.route("/youtube/predictviews/<string:name>")
@login_required

def predictViews(name):
    
    length = request.args.get('dur')
    cat = request.args.get('category_id')
    
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
    

    varV1 = 0.00156376762
    varV2 = 2.08209400
    varV3 = 0.0134076844
    varV4 = 0.0000533043632
    varV5 = -0.0107301493
    varV6 = -0.00151770880
    
    
    varL1 = 0.000491893046
    varL2 = 0.082029009
    varL3 = 0.00648799428
    varL4 = 0.0000146301918
    varL5 = -0.00216844026
    varL6 = -0.00053356926
    
    try:
        Cid,vid,view,sub,name,description,Date,privacy,featured,colour,bannerurl,location,customurl,language = getChannelData(name)
    
    except:
        flash("Couldn't get data. Please check whether entered details are correct","warning")
        return redirect(url_for('main.youtube'))
    
    Date = datetime.strptime(Date,'%Y-%m-%d').date()
    today = date.today()
    days = abs(Date-today).days

    viewPred = int(varV1*int(vid) + varV2*int(sub) + varV3*int(days) + varV4*int(view) + varV5*int(cat) + varV6*int(length))
    likePred = int(varL1*int(vid) + varL2*int(sub) + varL3*int(days) + varL4*int(view) + varL5*int(cat) + varL6*int(length))
    
    return render_template('predictviews.html', viewPred=viewPred,likePred=likePred,loginmodalshow= loginmodalshow, loginform = loginform, modalshow =modalshow,
                                                registerform=registerform)



@youtube.route("/youtube/viralvideoanalysis")
@login_required

def viralVideos():
    
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
        
        data = (pd.read_csv('social_media_analysis/youtube/codes/ViralVideoAnalysis/data.csv'))
        analyzedData = (pd.read_csv('social_media_analysis/youtube/codes/ViralVideoAnalysis/analysedData.csv'))
        
        language = data.iloc[:,7].values
        location = data.iloc[:,14].values
        category = data.iloc[:,6].values
        likePerc = data.iloc[:,15].values[:15]
        dislikePerc = data.iloc[:,16].values[:15]
        likeDisRatio = data.iloc[:,17].values[:15]
       
        
        languagePair=[]
        locationPair=[]
        categoryPair=[]
    
        dur = analyzedData.iloc[:,1].values
        sub = (analyzedData.iloc[:,4].values)[:6]
        vid = (analyzedData.iloc[:,3].values)[:6]
        days = (analyzedData.iloc[:,2].values)[:7]
        views = (analyzedData.iloc[:,5].values)[:7]
        
        
        for lan in sorted(set(language)):
            count = list(language).count(lan)
            #print(lan,count)
            languagePair.append([lan,count])
        
        for loc in sorted(set(location)):
            count = list(location).count(loc)
            #print(loc,count)
            locationPair.append([loc,count])
    
        for cat in sorted(set(category)):
            count = list(category).count(cat)
            #print(cat,count)
            categoryPair.append([cat,count])
    
            
        return render_template('viralVideo.html', loginmodalshow= loginmodalshow, loginform = loginform, modalshow =modalshow, registerform=registerform,
                               languagePair=languagePair,locationPair=locationPair,categoryPair=categoryPair,likePerc=likePerc,dislikePerc=dislikePerc,
                               likeDisRatio=likeDisRatio,dur=dur,sub=sub,vid=vid,days=days,views=views)
    
    except:
        flash('Something went wrong. Please try again.','warning')
        return redirect(url_for('main.youtube'))
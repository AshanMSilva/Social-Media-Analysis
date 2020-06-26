#import sentiment_mod as s
import urllib.request
import json
from textblob import TextBlob


#key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
key = "AIzaSyCbfK6-IwYr-jGjB595C8MkyC54J1jwdaA"



def getComments(Vid):
    
    
    comments = []
    replyCount = 0
    hasnextpage = False
    
    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=" + Vid + "&key=" + key + "&maxResults=100"
    data = (urllib.request.urlopen(url)).read()
    
    #print(url)
    numComment = len(json.loads(data)['items'])
    for comment in range(numComment):
        comments.append(json.loads(data)['items'][comment]["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
        replyCount = replyCount + int(json.loads(data)['items'][comment]["snippet"]["totalReplyCount"])
    
    try:
        token = json.loads(data)["nextPageToken"]
        hasnextpage = True
        
    except KeyError:
        return comments,replyCount

    while hasnextpage:
        url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=" + Vid + "&key=" + key + "&maxResults=100" + "&pageToken=" + token 
        data = (urllib.request.urlopen(url)).read()
        numComment = len(json.loads(data)['items'])
        for comment in range(numComment):
            comments.append(json.loads(data)['items'][comment]["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
            replyCount = replyCount + int(json.loads(data)['items'][comment]["snippet"]["totalReplyCount"])

        try:
            token = json.loads(data)["nextPageToken"]
            hasnextpage = True
        
        except KeyError:
            return comments,replyCount


def sentimentAnalysis(comment):
    
    emojis = ["👏🏽","👌", "♥️","👍","😍","😀","🔥","💪","✌️","😘","❤","😊"]
    for emoji in emojis:
        if emoji in comment:
            return 1
        
    tb = TextBlob(comment)
    sent  = tb.sentiment.polarity
    if sent>0.1:
        return 1
    if sent<-0.1:
        return -1
    if -0.1<=sent<=0.1:
        return 0
  
#Vid = input("enter id")
#print(getComments(Vid))
#print(len(comments),replyCount)
#for comment in comments:
    #print(comment,sentimentAnalysis(comment))


#for comment in comments:
    #print(s.sentiment(comment))
#import sentiment_mod as s
import urllib.request
import json
from textblob import TextBlob


#key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
key = "AIzaSyCbfK6-IwYr-jGjB595C8MkyC54J1jwdaA"



def getComments(Vid,nextPage):
    
    comments = []
    replyCount = 0
    
    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=" + Vid + "&key=" + key + "&maxResults=100" + "&pageToken=" + nextPage 
    data = (urllib.request.urlopen(url)).read()
    #global replyCount
    
    #print(url)
    numComment = len(json.loads(data)['items'])
    try:
        token = json.loads(data)["nextPageToken"]
    except KeyError:
        for comment in range(numComment):
            comments.append(json.loads(data)['items'][comment]["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
            #print(json.loads(data)['items'][comment]["snippet"]["totalReplyCount"])
            replyCount = replyCount + int(json.loads(data)['items'][comment]["snippet"]["totalReplyCount"])
        #print(len(comments),replyCount)
        return comments,replyCount
    for comment in range(numComment):
        comments.append(json.loads(data)['items'][comment]["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
        replyCount+=int(json.loads(data)['items'][comment]["snippet"]["totalReplyCount"])
    getComments(Vid,token)

def sentimentAnalysis(comment):
    
    tb = TextBlob(comment)
    sent  = tb.sentiment.polarity
    if sent>0.1:
        return 1
    if sent<0.1:
        return -1
    else:
        return 0
        
#Vid = input("enter id")
#getComments(Vid,' ')
#print(len(comments),replyCount)
#for comment in comments:
    #print(comment,sentimentAnalysis(comment))


#for comment in comments:
    #print(s.sentiment(comment))
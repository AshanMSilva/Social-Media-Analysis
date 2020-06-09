import urllib.request
import json
import isodate

key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
parts = ['statistics','snippet']

def getChannelData(Cid):
    url = "https://www.googleapis.com/youtube/v3/channels?part="
    for part in parts :
        url+=part + ','
    url=url[:-1]
    url+= "&id=" + Cid + "&key=" + key
    #print(url)
    data = (urllib.request.urlopen(url)).read()
  
    date = json.loads(data)['items'][0]["snippet"]["publishedAt"]
    date = date[:10]
    sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    view = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    vid = int(json.loads(data)["items"][0]["statistics"]["videoCount"])
    try:
        location = json.loads(data)['items'][0]["snippet"]["country"]
    except KeyError:
        location = "Not specified"
     
    return vid,view,sub,date,location

def getVideoDetails(Vid):
    
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=" + Vid + "&key=" + key
    data = (urllib.request.urlopen(url)).read()
    
     
    date = json.loads(data)['items'][0]["snippet"]["publishedAt"]
    date = date[:10]
    
    categoryID = json.loads(data)['items'][0]["snippet"]["categoryId"]
    
    try:
        language = json.loads(data)['items'][0]["snippet"]["defaultLanguage"]
    except KeyError:
        language = "Not specified"
        
    duration = json.loads(data)['items'][0]["contentDetails"]["duration"]
    duration = isodate.parse_duration(duration)
    
    channel = json.loads(data)['items'][0]["snippet"]["channelId"]
    views = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    
    try:
        likes = int(json.loads(data)['items'][0]["statistics"]["likeCount"])
    except KeyError:
        likes=0
        
    try:
        dislikes = int(json.loads(data)['items'][0]["statistics"]["dislikeCount"])
    except KeyError:
        dislikes = 0
    try:
        comments = int(json.loads(data)['items'][0]["statistics"]["commentCount"])
    except KeyError:
        comments=0
    return channel,date,categoryID,language,duration,views,likes,dislikes,comments



def getVideoCategory(catId):
    
    url = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id=" + catId + "&key=" + key
    data = (urllib.request.urlopen(url)).read()
    category = json.loads(data)['items'][0]["snippet"]["title"]
    return category
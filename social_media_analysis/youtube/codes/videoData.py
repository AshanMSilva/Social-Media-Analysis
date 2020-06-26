import urllib.request
import json
import isodate


#key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
key = "AIzaSyCbfK6-IwYr-jGjB595C8MkyC54J1jwdaA"

def getVideoDetails(Vid):
    
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,status,statistics&id=" + Vid + "&key=" + key
    data = (urllib.request.urlopen(url)).read()
    
    title = json.loads(data)['items'][0]["snippet"]["title"]
    des = json.loads(data)['items'][0]["snippet"]["description"]
    date = json.loads(data)['items'][0]["snippet"]["publishedAt"]
    date = date[:10]
    
    channel = json.loads(data)['items'][0]["snippet"]["channelId"]
    categoryID = json.loads(data)['items'][0]["snippet"]["categoryId"]
    
    try:
        language = json.loads(data)['items'][0]["snippet"]["defaultLanguage"]
    except KeyError:
        language = "Not specified"
        
    duration = json.loads(data)['items'][0]["contentDetails"]["duration"]
    duration = isodate.parse_duration(duration)
    
    status = json.loads(data)['items'][0]["status"]["uploadStatus"]
    status = status.capitalize()
    
    privacy = json.loads(data)['items'][0]["status"]["privacyStatus"]
    privacy = privacy.capitalize()
    
    views = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    likes = int(json.loads(data)['items'][0]["statistics"]["likeCount"])
    dislikes = int(json.loads(data)['items'][0]["statistics"]["dislikeCount"])
    
    return title,des,date,channel,categoryID,language,duration,privacy,status,views,likes,dislikes

def getVideoCategory(catId):
    
    url = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id=" + catId + "&key=" + key
    data = (urllib.request.urlopen(url)).read()
    category = json.loads(data)['items'][0]["snippet"]["title"]
    return category

#getVideoDetails("-n2XQE0T3QU")
#print(getVideoCategory("28"))
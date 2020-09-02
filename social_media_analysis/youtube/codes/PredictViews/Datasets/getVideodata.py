import urllib.request
import json
import isodate


key = "AIzaSyAKR5zwKAvaqQDKaMsfdLSmIsJ_oJGebUk"
#key = "AIzaSyCbfK6-IwYr-jGjB595C8MkyC54J1jwdaA"


def getVideoDetails(Vid):
    
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=" + Vid + "&key=" + key
    #print(url)
    try:
        data = (urllib.request.urlopen(url)).read()
    except urllib.request.HTTPError:
        channel=categoryID=dur=views=likes= "N/A"
        return channel,categoryID,dur,views,likes
     
    try:
        channel = json.loads(data)['items'][0]["snippet"]["channelId"]
    except (IndexError,KeyError):
        channel=categoryID=dur=views=likes= "N/A"
        return channel,categoryID,dur,views,likes
    categoryID = int(json.loads(data)['items'][0]["snippet"]["categoryId"])
    
 
        
    duration = json.loads(data)['items'][0]["contentDetails"]["duration"]
    duration = isodate.parse_duration(duration)
    dur = duration.total_seconds()
    
    try:
        views = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    except KeyError:
        views = "N/A"
        
    try:
        likes = int(json.loads(data)['items'][0]["statistics"]["likeCount"])
    except KeyError:
        likes = "N/A"
    
    
    return channel,categoryID,dur,views,likes


#print(getVideoDetails("-n2XQE0T3QU"))
#print(getVideoCategory("28"))
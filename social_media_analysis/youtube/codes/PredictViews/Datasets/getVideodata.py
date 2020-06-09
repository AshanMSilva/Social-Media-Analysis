import urllib.request
import json
import isodate


key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"


def getVideoDetails(Vid):
    
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=" + Vid + "&key=" + key
    #print(url)
    try:
        data = (urllib.request.urlopen(url)).read()
    except urllib.request.HTTPError:
        channel=categoryID=dur=views=likes=comments= "N/A"
        return channel,categoryID,dur,views,likes,comments
     
    try:
        channel = json.loads(data)['items'][0]["snippet"]["channelId"]
    except (IndexError,KeyError):
        channel=categoryID=dur=views=likes=comments= "N/A"
        return channel,categoryID,dur,views,likes,comments
    categoryID = int(json.loads(data)['items'][0]["snippet"]["categoryId"])
    
 
        
    duration = json.loads(data)['items'][0]["contentDetails"]["duration"]
    duration = isodate.parse_duration(duration)
    dur = duration.total_seconds()
    
    
    views = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    
    try:
        likes = int(json.loads(data)['items'][0]["statistics"]["likeCount"])
    except KeyError:
        likes = "N/A"
    try:
        comments = int(json.loads(data)['items'][0]["statistics"]["commentCount"])
    except KeyError:
        comments="N/A"
    
    return channel,categoryID,dur,views,likes,comments


#print(getVideoDetails("-n2XQE0T3QU"))
#print(getVideoCategory("28"))
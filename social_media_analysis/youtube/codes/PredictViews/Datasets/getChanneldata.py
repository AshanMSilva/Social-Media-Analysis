import urllib.request

import json
from datetime import date
import isodate

key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
#key = "AIzaSyCbfK6-IwYr-jGjB595C8MkyC54J1jwdaA"

parts = ['statistics','snippet']

def getChannelData(Cid):
    url = "https://www.googleapis.com/youtube/v3/channels?part="
    for part in parts :
        url+=part + ','
    url=url[:-1]
    url+= "&id=" + Cid + "&key=" + key
    #print(url)
    
    try:
        data = (urllib.request.urlopen(url)).read()
    except urllib.request.HTTPError:
        vid=view=sub=time= "N/A"
        return vid,view,sub,time
    
    try:
        joinDate = json.loads(data)['items'][0]["snippet"]["publishedAt"]
        joinDate = isodate.parse_date(joinDate)
        time = (date.today()-joinDate).days
    except (IndexError,KeyError):
        vid=view=sub=time= "N/A"
        return vid,view,sub,time
    
    try:
        sub = int(json.loads(data)['items'][0]["statistics"]["subscriberCount"])
    except KeyError:
        sub = "N/A"
    
    try:
        view = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    except KeyError:
        view = "N/A"
    try:
        vid = int(json.loads(data)["items"][0]["statistics"]["videoCount"])
    except KeyError:
        vid = "N/A"
        
    return vid,view,sub,time
    
#Cid = input("enter id")
#print(getChannelData("UC98x5I1LVPhtnUHDyujq7zg"))

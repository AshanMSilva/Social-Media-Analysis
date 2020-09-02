import urllib.request
import json

#key = "AIzaSyDPgpf4oaUa5dbzkvQlVd9eNiyF4zsThA8"
key = "AIzaSyDlN73Iv4q9MA1DSVco_o3Gl0L4504K44U"
parts = ['statistics','snippet','brandingSettings','status']

def getChannelData(Cid):
    url = "https://www.googleapis.com/youtube/v3/channels?part="
    for part in parts :
        url+=part + ','
    url=url[:-1]
    url+= "&id=" + Cid + "&key=" + key
    #print(url)
    data = (urllib.request.urlopen(url)).read()
    
    name = json.loads(data)['items'][0]["snippet"]["title"]
    description = json.loads(data)['items'][0]["snippet"]["description"]
    date = json.loads(data)['items'][0]["snippet"]["publishedAt"]
    date = date[:10]
    privacy = json.loads(data)['items'][0]["status"]["privacyStatus"]
    try:
        featured = json.loads(data)['items'][0]["brandingSettings"]["channel"]["featuredChannelsUrls"]
    except KeyError:
        featured = "0"
    colour = json.loads(data)['items'][0]["brandingSettings"]["channel"]["profileColor"]
    bannerurl =json.loads(data)['items'][0]["snippet"]["thumbnails"]["default"]["url"]
    sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    view = int(json.loads(data)['items'][0]["statistics"]["viewCount"])
    vid = int(json.loads(data)["items"][0]["statistics"]["videoCount"])
    try:
        customurl = json.loads(data)['items'][0]["snippet"]["customUrl"]
    except KeyError:
        customurl='Not Available'
    try:
        location = json.loads(data)['items'][0]["snippet"]["country"]
    except KeyError:
        location = "Not specified"
    try:
        language = json.loads(data)['items'][0]["snippet"]["defaultLanguage"]
        if language == "en":
            language = "English"
    except KeyError:
        language = "Not specified"
    return Cid,vid,view,sub,name,description,date,privacy,featured,colour,bannerurl,location,customurl,language
    
#Cid = input("enter id")
#print(getChannelData(Cid))

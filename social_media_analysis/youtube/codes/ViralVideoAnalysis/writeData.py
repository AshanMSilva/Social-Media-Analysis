from getdata import getChannelData,getVideoDetails,getVideoCategory
import pandas as pd
import sys

ids = (pd.read_csv('ids.csv'))
ids = ids.iloc[:,1].values


subCount=[]
vidCount=[]
totalViewCount=[]
channelDate=[]
channelLocation=[]
uploadedDate=[]
categoryList=[]
videoLanguage=[]
duration=[]
viewCount=[]
likeCount=[]
dislikeCount=[]
commentCount=[]
c=0

for Vid in ids:
    
    channel,date,categoryID,language,dur,views,likes,dislikes,comments = getVideoDetails(Vid)
    
    category = getVideoCategory(categoryID)
    print(date)
    uploadedDate.append(date)
    categoryList.append(category)
    videoLanguage.append(language)
    duration.append(dur)
    viewCount.append(views)
    likeCount.append(likes)
    dislikeCount.append(dislikes)
    commentCount.append(comments)
    
    vid,view,sub,date,location = getChannelData(channel)
    print(date)
    subCount.append(sub)
    vidCount.append(vid)
    totalViewCount.append(view)
    channelDate.append(date)
    channelLocation.append(location)
    
    c+=1
    print(c)
    
    sys.exit()
df = pd.DataFrame({'ChannelID':ids,'ViewCount':viewCount, 'likeCount':likeCount, 'dislikeCount':dislikeCount, 'uploadedDate':uploadedDate,
                   'category':categoryList, 'videoLanguage':videoLanguage,'duration':duration,'commentCount':commentCount, 'subCount':subCount,
                   'TotalViewCount':totalViewCount,'VideoCount':vidCount, 'channelDate':channelDate,'channelLocation':channelLocation}).to_csv('data.csv')
    
    
    
    
   

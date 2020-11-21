from getdata import getChannelData,getVideoDetails,getVideoCategory
import pandas as pd


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
titles=[]

#len(ids)
for i in range(245,400):
    
    channel,date,categoryID,language,dur,views,likes,dislikes,comments,title = getVideoDetails(ids[i])
    
    category = getVideoCategory(categoryID)
    
    uploadedDate.append(date)
    categoryList.append(category)
    videoLanguage.append(language)
    duration.append(dur)
    viewCount.append(views)
    likeCount.append(likes)
    dislikeCount.append(dislikes)
    commentCount.append(comments)
    titles.append(title)
    
    print(channel)
    vid,view,sub,date,location = getChannelData(channel)
    
    subCount.append(sub)
    vidCount.append(vid)
    totalViewCount.append(view)
    channelDate.append(date)
    channelLocation.append(location)
    

    print(i)
    
    
df = pd.DataFrame({'ChannelID':ids[245:400],'ViewCount':viewCount, 'likeCount':likeCount, 'dislikeCount':dislikeCount, 'uploadedDate':uploadedDate,
                   'category':categoryList, 'videoLanguage':videoLanguage,'duration':duration,'commentCount':commentCount, 'subCount':subCount,
                   'TotalViewCount':totalViewCount,'VideoCount':vidCount, 'channelDate':channelDate,'channelLocation':channelLocation,'title':titles}).to_csv('data.csv',mode='a',header=False)
    
    
    
    
   

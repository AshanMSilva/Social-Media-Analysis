import pandas as pd
from getChanneldata import  getChannelData
from getVideodata import  getVideoDetails



category=[]
duration=[]
viewsList=[]
likesList=[]
commentsList=[]
videos=[]
subs=[]
totViews=[]
timeList=[]

data = (pd.read_csv('data.csv'))

ids = data.iloc[:,1].values


for i in range(0,len(ids),80):
    
    channel,categoryID,dur,views,likes,comments = getVideoDetails(ids[i])
    
    if channel=="N/A":
        vid=view=sub=time= "N/A"
    else:
        vid,view,sub,time = getChannelData(channel)  
    category.append(categoryID)
    duration.append(dur)
    viewsList.append(views)
    likesList.append(likes)
    commentsList.append(comments)
    videos.append(vid)
    subs.append(sub)
    totViews.append(view)
    timeList.append(time)
    print(i,category)

df = pd.DataFrame({'ViewCount':viewsList, 'likeCount':likesList,'date':timeList,'category':category,'duration':duration,'commentCount':commentsList,
                   'subCount':subs,'TotalViewCount':totViews,'VideoCount':videos}).to_csv('datapredictviews.csv')

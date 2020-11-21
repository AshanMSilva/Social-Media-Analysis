# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:32:15 2020

@author: user
"""


import pandas as pd
     
data = (pd.read_csv('data.csv'))

#ghiklmopqrst


#piechart
#language = data.iloc[:,7].values
#location = data.iloc[:,14].values
#category = data.iloc[:,6].values

#worm
#likePerc = data.iloc[:,15].values
#dislikePerc = data.iloc[:,16].values
#likeDisRatio = data.iloc[:,17].values

#histogram
duration = data.iloc[:,8].values
#commentsPerView = data.iloc[:,19].values



#bargraph
sub = data.iloc[:,10].values
totalView = data.iloc[:,11].values
videoCount = data.iloc[:,12].values
daysToPublish = data.iloc[:,18].values

dur0_1=0
dur1_2=0
dur2_3=0
dur3_4=0
dur4_5=0
dur5_6=0
dur6_7=0
dur7_8=0
dur8_9=0
dur9_10=0
dur10=0

dur_out=[]

for dur in duration:
   
    if int(dur[7:9])==0:
        if int(dur[10:12])==0:
            dur0_1+=1
        if int(dur[10:12])==1:
            dur1_2+=1
        if int(dur[10:12])==2:
            dur2_3+=1
        if int(dur[10:12])==3:
            dur3_4+=1
        if int(dur[10:12])==4:
            dur4_5+=1
        if int(dur[10:12])==5:
            dur5_6+=1
        if int(dur[10:12])==6:
            dur6_7+=1
        if int(dur[10:12])==7:
            dur7_8+=1
        if int(dur[10:12])==8:
            dur8_9+=1
        if int(dur[10:12])==9:
            dur9_10+=1
            
        else:
            dur10=0
    else:
        dur10+=1        

dur_out.append([dur0_1,dur1_2,dur2_3,dur3_4,dur4_5,dur5_6,dur6_7,dur7_8,dur8_9,dur9_10,dur10])
print(dur_out)

totView1=0
totView2=0
totView3=0
totView4=0
totView5=0
totView6=0
totView7=0

totView_out=[]

for count in  totalView:
    if count<1000000000:
        totView1+=1
    if 1000000000 <= count < 10000000000:
        totView2+=1
    if 10000000000 <= count < 20000000000:
        totView3+=1
    if 20000000000 <= count < 30000000000:
        totView4+=1
    if 30000000000 <= count < 40000000000:
        totView5+=1
    if 40000000000 <= count < 50000000000:
        totView6+=1
    if count > 50000000000:
        totView7+=1


totView_out.append([totView1,totView2,totView3,totView4,totView5,totView6,totView7,"null","null","null","null"])


sub1=0
sub2=0
sub3=0
sub4=0
sub5=0
sub6=0

subCount_out=[]

for count in sub:
    if count<100000:
        sub1+=1
    if 100000 <= count < 500000:
        sub2+=1
    if 500000 <= count < 1000000:
        sub3+=1
    if 1000000 <= count < 20000000:
        sub4+=1
    if 20000000 <= count < 50000000:
        sub5+=1
    if count > 50000000:
        sub6+=1
        
        
subCount_out.append([sub1,sub2,sub3,sub4,sub5,sub6,"null","null","null","null","null"])



com20=0
com100=0
com500=0
com1000=0
com2000=0
comi=0


com_out2=[]

for count in videoCount:
    if count<20:
        com20+=1
    if 20 <= count< 100:
        com100+=1
    if 100 <= count< 500:
        com500+=1
    if 500 <= count< 1000:
        com1000+=1
    if 1000 <= count< 2000:
        com2000+=1
    if count> 2000:
        comi+=1

com_out2.append([com20,com100,com500,com1000,com2000,comi,"null","null","null","null","null"])

com30=0
com90=0
com1=0
com2=0
com5=0
com10=0
comi=0

com_out3=[]

for count in daysToPublish:
    if int(count)<30:
        com30+=1
    if 30 <= int(count) < 90:
        com90+=1
    if 90 <= int(count)< 365:
        com1+=1
    if 365 <= int(count)< 730:
        com2+=1
    if 730 <= int(count)< 1825:
        com5+=1
    if 1825 <= int(count)< 3650:
        com10+=1
    if int(count)> 3650:
        comi+=1

com_out3.append([com30,com90,com1,com2,com5,com10,comi,"null","null","null","null"])


df = pd.DataFrame({'duration':dur_out[0],'daysToPublish':com_out3[0],'videoCount':com_out2[0],'sub':subCount_out[0],
                   'totalView':totView_out[0]}).to_csv('analysedData.csv')
 



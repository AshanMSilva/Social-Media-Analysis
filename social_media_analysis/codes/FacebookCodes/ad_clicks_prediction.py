import pickle
import pandas as pd 
import random

###sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.corpus import webtext 
from nltk.stem.porter import PorterStemmer 
from nltk.stem.wordnet import WordNetLemmatizer 
import nltk
import operator


class AdPrediction():
    def predict(self,input_data):
        filename = 'fbAdsModelNew.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        # f.seek(0)\
        result = loaded_model.predict(input_data)
        return result
    def impressions_from_money(self,money):  #input in usd
        return int(money*16.93*8.21)
    def rub_to_usd(self,rub):
        return rub/16.93
    def usd_to_rub(self,usd):
        return int(usd*16.93)
    def get_ad_text_result(self,text):
        word=text
        sent_tokenizer = PunktSentenceTokenizer(text) 
        sents = sent_tokenizer.tokenize(text) 
        porter_stemmer = PorterStemmer()

        nltk_tokens = nltk.word_tokenize(text) 
        wordnet_lemmatizer = WordNetLemmatizer() 
        nltk_tokens = nltk.word_tokenize(text) 

        text = nltk.word_tokenize(text)
        sid = SentimentIntensityAnalyzer() 
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

        scores = sid.polarity_scores(word)
        c= scores['compound']
        del scores['compound']

        res=max(scores.items(), key=operator.itemgetter(1))[0]
        # comments[i].append(c)
        # comments[i].append(scores)
        if(res=='neu'):
            return 1
        elif(res=='pos'):
            return 2
        elif(res=='neg'):
            return 3
class AdImpressionPrediction():
    def predict(self,input_data):
        filename = 'social_media_analysis\codes\FacebookCodes\\fbAdsImpreModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(input_data) 
        return result
 
class BestSolutions():
    def getBestGender(self,input_data,model):
        input_data['male']=1
        input_data['female']=0
        input_data['all']=0
        final_features=pd.DataFrame.from_dict(input_data)
        male_result= model.predict(final_features)   

        input_data['male']=0
        input_data['female']=1
        input_data['all']=0
        final_features=pd.DataFrame.from_dict(input_data)
        female_result= model.predict(final_features)            
        
          
        
        input_data['male']=0
        input_data['female']=0
        input_data['all']=1
        final_features=pd.DataFrame.from_dict(input_data)
        all_result= model.predict(final_features) 

        return [int(male_result),int(female_result),int(all_result)]

    def getBestSpend(self,input_data,clicks_model,prev_clicks):
        spend_results=[]
        true_usd=input_data['AdSpends'][0]  #usd
        first_usd=int(true_usd+1)
        final_clicks_list=[]
        final_money_list=[]

        cal_money_list=[true_usd]
        cal_cliks_list=[prev_clicks]

        spend_results.append([true_usd,prev_clicks])  #######
        for i in range(1,4):  #predict main values
            money=first_usd+10*i/4
            input_data['AdSpends']=int(money*16.93)  #usd to rub
            ad_prediction_temp=AdPrediction()
            impressions=ad_prediction_temp.impressions_from_money(money)
            input_data['AdImpressions']=impressions
            final_features=pd.DataFrame.from_dict(input_data)
            clicks=int(clicks_model.predict(final_features)[0])
            cal_money_list.append(int(money))
            cal_cliks_list.append(clicks)   


        for i in range(1,4):  #check main values
            if(cal_cliks_list[i]<cal_cliks_list[i-1]):
                cal_cliks_list[i]=cal_cliks_list[i-1]

        for i in range(first_usd*10,first_usd*10+80,5):  #calculate middle values
            money=i/10  #usd
            if(money in cal_money_list):
                final_clicks_list.append(cal_cliks_list[cal_money_list.index(money)])
                final_money_list.append(money)
                spend_results.append([money,cal_cliks_list[cal_money_list.index(money)]])
                continue
            for t in range(1,4):
                if(money<cal_money_list[t]):
                    y1=cal_cliks_list[t-1]
                    sq=money**2
                    tgap=cal_money_list[t]**2-cal_cliks_list[t]
                    
                    clicks=sq-tgap
                    if(clicks<y1):
                        clicks=y1
                    spend_results.append([money,int(clicks)])
                    final_clicks_list.append(int(clicks))
                    break
        return spend_results

    def getBestWeekDay(self,input_data,model,prev_day,prev_clicks):
        week_day_results={}
        calculated_list={}
        days=['sun','mon','tue','wed','thu','fri','sat']
        days_3=['mon','wed','fri']
        days_4=['sun','tue','thu','sat']
        days_need=[]
        days
        if(prev_day in days_4):
            days_4.remove(prev_day)
            days_need=days_4
        if(prev_day in days_3):
            days_3.remove(prev_day)
            days_3.append('sun')
            days_need=days_3

        #set all days as zero
        for day in days:
            input_data[day]=0
        for day in days_need:
            input_data[day]=1 
            final_features=pd.DataFrame.from_dict(input_data)
                 
            temp_res=int(model.predict(final_features)[0])
            calculated_list[day]=temp_res
            input_data[day]=0
        calculated_list[prev_day]=prev_clicks
        final_list=self.weekday_set(calculated_list,prev_day)
        return final_list

    def weekday_set(self,known_days,prev_day):
        days=['sun','mon','tue','wed','thu','fri','sat']
        days_3=['mon','wed','fri']
        days_4=['sun','tue','thu','sat']
        if(prev_day in days_4):
            known_days
            known_days['mon']=int((int(known_days['sun'])+int(known_days['tue']))/2)
            known_days['wed']=int((int(known_days['tue'])+int(known_days['thu']))/2)
            known_days['fri']=int((int(known_days['thu'])+int(known_days['sat']))/2)
            return known_days
        elif(prev_day in days_3):
            known_days
            known_days['tue']=int((int(known_days['mon'])+int(known_days['wed']))/2)
            known_days['thu']=int((int(known_days['wed'])+int(known_days['fri']))/2)
            known_days['sat']=int((int(known_days['fri'])+int(known_days['sun']))/2)
            return known_days


    def adspend_check(self,prev):
        stt=prev[0]+100
        for i in range(1,len(prev)):
            if(stt<prev[i]):
                # print(prev[i])
                next_correct_index=i-1
                for j in range(i+1,len(prev)):
                    if(stt>prev[j]):
                        next_correct_index=j
                        break
                prev[i]=(prev[i-1]+prev[next_correct_index])/2
        for i in range(1,len(prev)):
            gap=prev[i]-prev[i-1]
            if(gap<0):
                prev[i]=prev[i-1]+random.choice([1,0])
                
        return prev
            

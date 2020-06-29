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
        filename = 'social_media_analysis/codes/FacebookCodes/fbAdsModelNew.sav'
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

    def getBestSpend(self,input_data,clicks_model):
        spend_results=[]
        true_rub=input_data['AdSpends'][0]  #rub
        true_usd=true_rub/16.93
        first_usd=int(true_usd)+1
        clicks_list=[]
        money_list=[]
        for i in range(first_usd*10,first_usd*10+155,5):
            money=i/10  #usd
            money_list.append(money)
            input_data['AdSpends']=int(money*16.93)  #usd to rub
            ad_prediction_temp=AdPrediction()
            impressions=ad_prediction_temp.impressions_from_money(money)
            input_data['AdImpressions']=impressions

            final_features=pd.DataFrame.from_dict(input_data)
            clicks=int(clicks_model.predict(final_features)[0])
            clicks_list.append(clicks)
            # clicks=int((clicks_model.predict(final_features)[0]**2)**0.5)
            # spend_results.append([money,clicks])
        clicks_list_new=self.adspend_check(clicks_list)
        for i in range(len(money_list)):
            spend_results.append([money_list[i],clicks_list_new[i]])
        return spend_results

    def getBestWeekDay(self,input_data,model):
        week_day_results={}
        check_list=[]
        days=['sun','mon','tue','wed','thu','fri','sat']
        #set all days as zero
        for day in days:
            input_data[day]=0
        for day in days:
            input_data[day]=1
            final_features=pd.DataFrame.from_dict(input_data)
            # week_day_results[day]=int((model.predict(final_features)[0]**2)**0.5)

            temp_res=int(model.predict(final_features)[0])
            check_list.append(temp_res)
            # week_day_results[day]=int(model.predict(final_features)[0])
            input_data[day]=0
        checked_list=self.weekday_check(check_list)
        for i in range(7):
            week_day_results[days[i]]=int(checked_list[i])
        return week_day_results

    def weekday_check(self,prev):
        true_av=sum(prev)/len(prev)
        for i in range(len(prev)):
            if prev[i]>true_av*2 :
                prev[i]=true_av
                true_av=sum(prev)/len(prev)
        return prev

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
            

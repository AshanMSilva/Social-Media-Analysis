import pickle
import pandas as pd 

class AdPrediction():
    def predict(self,input_data):
        # filename = 'social_media_analysis\codes\FacebookCodes\\facebooklik\.csv'
        # f = 
        filename = 'social_media_analysis\codes\FacebookCodes\\fbAdsModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        # f.seek(0)\
        result = loaded_model.predict(input_data)
        return result

class AdImpressionPrediction():
    def predict(self,input_data):
        # filename = 'social_media_analysis\codes\FacebookCodes\\facebooklik\.csv'
        # f = 
        filename = 'social_media_analysis\codes\FacebookCodes\\fbAdsImpreModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        # f.seek(0)\
        result = loaded_model.predict(input_data)
        return result

# final={'mon':[mon] ,'tue':[tue] ,'wed':[wed] ,'thu':[thu] ,'fri':[fri] ,'sat':[sat] ,'sun':[sun] ,'male':[male] ,'female':[female] ,'all':[all] ,'TextWordCount':[len(txt.split())] ,'startAge':[startAge] ,'endAge':[endAge],'AdImpressions':[impre_output],'AdSpends':[adSpends] }
#  prediction_impre   
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
        return [int(female_result),int(male_result),int(all_result)]

    def getBestSpend(self,input_data,model):
        spend_results=[]
        first=int(input_data['AdSpends'][0])
        for money in range(first,first+301,10):
            input_data['AdSpends']=money
            final_features=pd.DataFrame.from_dict(input_data)
            spend_results.append([money,int(model.predict(final_features)[0])])
        return spend_results

    def getBestWeekDay(self,input_data,model):
        week_day_results={}
        days=['sun','mon','tue','wed','thu','fri','sat']
        #set all days as zero
        for day in days:
            input_data[day]=0
        for day in days:
            input_data[day]=1
            final_features=pd.DataFrame.from_dict(input_data)
            week_day_results[day]=int(model.predict(final_features)[0])
            input_data[day]=0
        return week_day_results
            
            
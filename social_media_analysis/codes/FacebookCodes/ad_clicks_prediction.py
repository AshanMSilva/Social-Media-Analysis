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
        return [int((male_result**2)**0.5),int((female_result**2)**0.5),int((all_result**2)**0.5)]

    def getBestSpend(self,input_data,clicks_model,impre_model):
        spend_results=[]
        first=int(input_data['AdSpends'][0])
        for money in range(first,first+301,10):
            input_data['AdSpends']=money
            final_features=pd.DataFrame.from_dict(input_data)
            impressions=int((impre_model.predict(final_features)[0]**2)**0.5)

            clicks_input_data=input_data
            del clicks_input_data['AdSpends']
            clicks_input_data['AdImpressions']=impressions
            clicks_input_data['AdSpends']=money
            clicks_final_features= pd.DataFrame.from_dict(clicks_input_data)
            clicks=int((clicks_model.predict(clicks_final_features)[0]**2)**0.5)
            del clicks_input_data['AdImpressions']
            spend_results.append([money,clicks,impressions])
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
            week_day_results[day]=int((model.predict(final_features)[0]**2)**0.5)
            input_data[day]=0
        return week_day_results
            
            
import pickle

class LikePrediction():
    def predict(self,input_data):
        # filename = 'social_media_analysis\codes\FacebookCodes\\facebooklik\.csv'
        # f = 
        filename = 'social_media_analysis\codes\FacebookCodes\\fbLikeModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        # f.seek(0)\
        result = loaded_model.predict(input_data)
        return result




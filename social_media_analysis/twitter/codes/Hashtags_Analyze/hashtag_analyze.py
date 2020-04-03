from collections import Counter
from textblob import TextBlob
import re

class HashtagAnalyzer():
	def divide_tweets_according_to_hours(self, tweets):
		zero=0
		one =0
		two=0
		three=0
		four=0
		five=0
		six=0
		seven=0
		eight=0
		nine=0
		ten=0
		eleven=0
		twelve=0
		thirteen=0
		fourteen=0
		fifteen=0
		sixteen=0
		seventeen=0
		eighteen=0
		nineteen=0
		twenty=0
		twentyone=0
		twentytwo=0
		twentythree=0
		for tweet in tweets:
			if(tweet.created_at.hour == 0):
			    zero+=1
			if(tweet.created_at.hour == 1):
			    one+=1
			if(tweet.created_at.hour == 2):
			        two+=1
			if(tweet.created_at.hour == 3):
				three+=1
			if(tweet.created_at.hour == 4):
			    four+=1
			if(tweet.created_at.hour == 5):
			    five+=1
			if(tweet.created_at.hour == 6):
			    six+=1
			if(tweet.created_at.hour == 7):
			    seven+=1
			if(tweet.created_at.hour == 8):
			    eight+=1
			if(tweet.created_at.hour == 9):
			    nine+=1
			if(tweet.created_at.hour == 10):
			    ten+=1
			if(tweet.created_at.hour == 11):
			    eleven+=1
			if(tweet.created_at.hour == 12):
			    twelve+=1
			if(tweet.created_at.hour == 13):
			    thirteen+=1
			if(tweet.created_at.hour == 14):
			    fourteen+=1
			if(tweet.created_at.hour == 15):
			    fifteen+=1
			if(tweet.created_at.hour == 16):
			    sixteen+=1
			if(tweet.created_at.hour == 17):
			    seventeen+=1
			if(tweet.created_at.hour == 18):
			    eighteen+=1
			if(tweet.created_at.hour == 19):
			    nineteen+=1
			if(tweet.created_at.hour == 20):
			    twenty+=1
			if(tweet.created_at.hour == 21):
			    twentyone+=1
			if(tweet.created_at.hour == 22):
			    twentytwo+=1
			if(tweet.created_at.hour == 23):
			    twentythree+=1
		hourdata ={
            "0":zero,
            "1":one,
            "2":two,
            "3":three,
            "4":four,
            "5":five,
            "6":six,
            "7":seven,
            "8":eight,
            "9":nine,
            "10":ten,
            "11":eleven,
            "12":twelve,
            "13":thirteen,
            "14":fourteen,
            "15":fifteen,
            "16":sixteen,
            "17":seventeen,
            "18":eighteen,
            "19":nineteen,
            "20":twenty,
            "21":twentyone,
            "22":twentytwo,
            "23":twentythree   
        }
		return hourdata
	def divide_tweets_according_to_months(self, tweets):
		jan =0
		feb=0
		mar=0
		apr=0
		may=0
		jun=0
		jul=0
		aug=0
		sep=0
		octo=0
		nov=0
		dec=0
		for tweet in tweets:
			if(tweet.created_at.month == 1):
			    jan+=1
			if(tweet.created_at.month == 2):
			        feb+=1
			if(tweet.created_at.month == 3):
			        mar+=1
			if(tweet.created_at.month == 4):
			    apr+=1
			if(tweet.created_at.month == 5):
			    may+=1
			if(tweet.created_at.month == 6):
			    jun+=1
			if(tweet.created_at.month == 7):
			    jul+=1
			if(tweet.created_at.month == 8):
			    aug+=1
			if(tweet.created_at.month == 9):
			    sep+=1
			if(tweet.created_at.month == 10):
			    octo+=1
			if(tweet.created_at.month == 11):
			    nov+=1
			if(tweet.created_at.month == 12):
			    dec+=1
		monthdata ={
            "1":jan,
            "2":feb,
            "3":mar,
            "4":apr,
            "5":may,
            "6":jun,
            "7":jul,
            "8":aug,
            "9":sep,
            "10":octo,
            "11":nov,
            "12":dec
        }
		return monthdata
	def divide_tweets_according_to_sentiment(self, tweets):
		positive = 0
		negative = 0
		results =[]
		for tweet in tweets:
			if(hasattr(tweet, 'retweeted_status')):
			    text = tweet.retweeted_status.full_text
			else:
			    text = tweet.full_text
			result = self.analyze_sentiment(text)
			results.append(result)
		for res in results:
			if(res == 1):
				positive+=1
			if(res == 0):
				negative +=1
		sentimentdata={
        	"positive": positive,
        	"negative": negative
        }
		return sentimentdata

	def clean_tweet(self, text):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

	def analyze_sentiment(self, text):
		analysis = TextBlob(self.clean_tweet(text))
            
		if analysis.sentiment.polarity > 0:
		    return 1
		elif analysis.sentiment.polarity == 0:
		    return 0
		else:
		    return -1
	def get_user_mentions(self, tweets):
		user_mentions=[]
		for tweet in tweets:
		    for t in tweet.entities['user_mentions']:
		        user_mentions.append(t['screen_name'])
		c = Counter(user_mentions)
		sortedlist = c.most_common()
		return sortedlist
	def get_user_hashtags(self, tweets):
		hashtags=[]
		for tweet in tweets:
		    for t in tweet.entities['hashtags']:
		        hashtags.append(t['text'])
		c = Counter(hashtags)
		sortedlist = c.most_common()
		return sortedlist
	def get_users(self, tweets):
		users=[]
		for tweet in tweets:
			users.append(tweet.user.screen_name)
		c = Counter(users)
		sortedlist = c.most_common()
		return sortedlist
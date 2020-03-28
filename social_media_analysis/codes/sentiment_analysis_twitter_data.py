# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 00:05:22 2020

@author: user
"""


from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from textblob import TextBlob
 
from social_media_analysis.codes import twitter_credentials

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    def get_statuses_lookup_tweets(self, num_tweets):
        statuses_lookup_tweets = []
        for tweet in Cursor(self.twitter_client.statuses_lookup, id=self.twitter_user).items(num_tweets):
            statuses_lookup_tweets.append(tweet)
        return statuses_lookup_tweets
    
    def get_retweets_of_me(self, num_tweets):
        retweets_of_me = []
        for tweet in Cursor(self.twitter_client.retweets_of_me, id=self.twitter_user).items(num_tweets):
            retweets_of_me.append(tweet)
        return retweets_of_me
    
    def get_mentions_timeline(self, num_tweets):
        mentions_timeline = []
        for mention in Cursor(self.twitter_client.mentions_timeline, id=self.twitter_user).items(num_tweets):
            mentions_timeline.append(mention)
        return mentions_timeline
    
    ### single tweet information
    
    def get_tweet_status(self, tweet_id):
        tweet_status = self.twitter_client.get_status(tweet_id)
        return tweet_status
    
    def get_retweeters_of_a_tweet(self, tweet_id):
        retweeters_ids = self.twitter_client.retweeters(tweet_id)
        return retweeters_ids
    
    def get_retweets_of_a_tweet(self, num_tweets,tweet_id):
        retweets = self.twitter_client.retweets(tweet_id)
        return retweets
    
    def get_user(self, name):
        user = self.twitter_client.get_user(name)
        return user
    
    def get_user_followers(self,name):
        followers = self.twitter_client.followers(name)
        return followers
    
    def get_search_users(self, name):
        users = self.twitter_client.search_users(name)
        return users
    
    def get_friendship_between_two_friends(self, first_name, second_name):
        friendship = self.twitter_client.show_friendship(first_name, second_name)
        return friendship
        
    def get_favorites(self,user_id):
        favorites= self.tweeter_client.favorites(user_id)
        return favorites
    
    def get_saved_search(self,user_id):
        saved_search = self.tweeter_client.get_saved_search(user_id)
        return saved_search
    
    def get_similar_tweets(self,tweet,result_type, num_tweets):   #mixed, recent, popular
        similar_tweets = self.twitter_client.search(tweet, result_type=result_type, count=num_tweets)
        return similar_tweets
    
    def get_trend_topic_locations(self, lat, long):
        locations = self.twitter_client.trends_closest(lat, long)
        return locations
    
    def get_location_info_by_geo_id(self, geo_id):
        place = self.twitter_client.geo_id(geo_id)
        return place

    def get_tweets_of_a_user(self, name, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, screen_name=name).items(num_tweets):
            tweets.append(tweet)
        return tweets
    

# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()    

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['text'] = np.array([tweet.text for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])

        return df
    
    def get_attribute_value_of_a_object(obj, attribute_name):
        return getattr(obj, attribute_name)

 
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    #tweets = api.user_timeline(screen_name="realDonaldTrump", count=20)

    #df = tweet_analyzer.tweets_to_data_frame(tweets)
    #df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    #print(df['id'])
    
    status = twitter_client.get_retweets_of_a_tweet(1,1237924658185469954)
    
    #print(dir(status[0]))
    #tweet = status[0]
    #print(getattr(tweet, 'text'))
    
    user = twitter_client.get_user('realDonaldTrump')
    
    #friendship = twitter_client.get_friendship_between_two_friends('AshanMSilva1','cse17mora')
    #print(friendship)
    
    search_results = twitter_client.get_similar_tweets('yesterday', 'recent')
    #print(search_results)
    print(getattr(search_results[0], 'text'))
    

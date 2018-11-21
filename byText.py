import config
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

#Tweepy auth configuration, keys are in config.py
auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

#Retrieving list of tweets (JSON) with those words in them.
tweets_s1 = api.search('Zuckerberg is')
tweets_s2 = api.search('Trump is')

#List that will handle each of the tweets's polarity
s1 = []
s2 = []

#For every tweet that says 'Zuckerberg is' it will append its polarity
#Polarity: -1 bad, 1 good, 0 neutral
for tweet in tweets_s1:
    s1.append(TextBlob(tweet.text).sentiment.polarity)

for tweet in tweets_s2:
    s2.append(TextBlob(tweet.text).sentiment.polarity)

#Plotting polarity for every set of tweets
plt.plot(s1)
plt.plot(s2)
plt.legend(['Zucc', 'Trump'])
plt.show()

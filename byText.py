import config
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

tweets_s1 = api.search('Zuckerberg is')
tweets_s2 = api.search('Trump is')

s1 = []
s2 = []

for tweet in tweets_s1:
    s1.append(TextBlob(tweet.text).sentiment.polarity)

for tweet in tweets_s2:
    s2.append(TextBlob(tweet.text).sentiment.polarity)

plt.plot(s1, 'ro')
plt.plot(s2, 'bo')
plt.legend(['Musk', 'Trump'])
plt.show()

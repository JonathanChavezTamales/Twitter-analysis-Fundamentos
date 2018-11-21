import config
import tweepy
import matplotlib.pyplot as plt
import re
from textblob import TextBlob

auth = tweepy.OAuthHandler(config.api_key, config.api_secret_key)
auth.set_access_token(config.access_token, config.access_token_secret)

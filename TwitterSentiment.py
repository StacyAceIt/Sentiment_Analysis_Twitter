#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:11:27 2018

@author: yolanda7zhang
"""

import tweepy
from textblob import TextBlob

exec(open("TwitterTokens.py").read())

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#API lets you access an apps functionality from code
#sentiment analysisi-> understanding and extracting feelings from data
api = tweepy.API(auth,wait_on_rate_limit = True)

'''
wiki = TextBlob("This movie is bad")

print(wiki.words)

print(wiki.tags)

print(wiki.sentiment.polarity)

wiki1 = TextBlob("This movie is very very bad")

print(wiki1.words)

print(wiki1.tags)

print(wiki1.sentiment.polarity)
'''
'''
gs = goslate.Goslate()
print(gs.translate('Hello world','zh'))
'''

def getSentiment(tweetset):
    sentlist = []
    #print(type(tweetset))
    for tweet in tweetset:        
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment,end = "\n\n")  
        sentlist.append(analysis.sentiment.polarity)
    #print(len(tweetset))
    return sentlist

def getTweets(place_id):
    tweets = api.search(q="crazy rich asian place:%s" % place_id, count = 100)
    tweetlist = []
    for tweet in tweets:
        tweetlist.append(tweet.text)
    #print(len(tweetlist))
    return tweetlist

def getSentiment2(tweetset):
    sentlist = []
    for tweet in tweetset:
        #print(tweet.text)
        analysis = TextBlob(tweet)
        #print(analysis.sentiment,end = "\n\n")  
        sentlist.append(analysis.sentiment.polarity)
    print("sample size: ",len(tweetset))
    return sentlist

def meanSent(sentlist):
    mean = sum(sentlist)/len(sentlist)
    return mean

# ISO 639-1 codes for lanugage names

print("Indonesia")
places = api.geo_search(query="Indonesia", granularity="country")
Indo_place_id = places[0].id
Itweets = getTweets(Indo_place_id)
#print(Itweets)
sentiment6 = getSentiment2(Itweets)                   
print("Mean sentiment: ",meanSent(sentiment6)) 


print("Brazil")
tweetset5 = api.search(q="crazy rich asians",geocode = "-23.5505,-46.6333,300km", count = 100)
sentiment5 = getSentiment(tweetset5)                   
print("Mean sentiment: ",meanSent(sentiment5))     


print("Mexico")
tweetset4 = api.search(q="crazy rich asians",geocode = "19.4326,-99.1332,300km", count = 100)
sentiment4 = getSentiment(tweetset4)                   
print("Mean sentiment: ",meanSent(sentiment4)) 

print("Singapore")
tweetset = api.search(q="crazy rich asians",geocode = "1.3521,103.8198,150km", count = 100)
tweets =[tweet for tweet in tweetset]
sentiment = getSentiment(tweets)                   
print("Mean sentiment: ",meanSent(sentiment))   


print("Malasia")
tweetset2 = api.search(q="crazy rich asians",geocode = "3.1390,101.6869,300km", count = 100)
sentiment2 = getSentiment(tweetset2)                   
print("Mean sentiment: ",meanSent(sentiment2))   

print("USA")
tweetset3 = api.search(q="crazy rich asians",geocode = "40.7128,-74.0060,1000km", count = 100)
sentiment3 = getSentiment(tweetset3)                   
print("Mean sentiment: ",meanSent(sentiment3)) 

#%%
#https://stackoverflow.com/questions/16592222/matplotlib-group-boxplots#
from pylab import plot, show, savefig, xlim, figure,hold, ylim, legend, boxplot, setp, axes

w = 0.5

bp = boxplot(sentiment,positions = [1],widths =w)
bp = boxplot(sentiment2,positions = [2],widths =w)
bp = boxplot(sentiment3,positions = [3],widths =w)
bp = boxplot(sentiment4,positions = [4],widths =w)
bp = boxplot(sentiment5,positions = [5],widths =w)
bp = boxplot(sentiment6,positions = [6],widths =w)

ax = axes()


xlim(0,7)
ylim(-1,1)
ax.set_xticklabels(['Singapore','Malasia','USA','Mexico','Brazil','Indonesia'])
ax.set_xticks([1,2,3,4,5,6])

#tweetset = api.search(q="Crazy Rich Asians")

#polarity is how positive or negative some text is [-1,1]
#1 very positive ; -1 very negative

#Subjectivity is how much of an opinion it is vs how factual [0,1]
#0 very objective, 1 very subjective

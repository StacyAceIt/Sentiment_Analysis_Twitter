#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:49:37 2018

@author: yolanda7zhang
"""
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


df = pd.read_csv("doubanComments.csv")
translation = df['Translation'].values.tolist()
comments = df['comments'].values.tolist()

msent=[]
for comment in comments:
    analysis = TextBlob(comment)
    msent.append(analysis.sentiment.polarity)

#print(type(translation))
#print(translation[-10:])

translation = [x for x in translation if "MYMEMORY WARNING" not in x]
print(len(translation))


Transent=[]
for comment in translation:
    analysis = TextBlob(comment)
    Transent.append(analysis.sentiment.polarity)
    #print(analysis.sentiment.polarity,end = "\n\n")


#print(sentiment)

df2 = pd.DataFrame(list(zip(comments,msent)),columns = ["comments","Sentiment"])
print(df2["Sentiment"].head())
print(df2.describe())

'''
print("Median  ",df2["TranslationSentiment"].median(),df2["Sentiment"].median())

df2.to_csv("doubanTranslate.csv")
# df2.plot.hist(alpha = 0.5)
plt.boxplot(df2["TranslationSentiment"].values)
df2.boxplot(column=['TranslationSentiment'],grid=True)
'''

#plt.boxplot(df2["Sentiment"].values)
df2.boxplot(column=['Sentiment'],grid=True)
df2.plot.hist()


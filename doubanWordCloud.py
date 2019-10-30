#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:26:52 2018

@author: yolanda7zhang
"""
# This file generates a word cloud from doubandata.txt

#generate word cloud
#referred to https://www.jianshu.com/p/d92a2b4aacb3

import jieba.analyse
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt

doubandata = open('doubanData.txt','r',encoding = 'utf-8')
comments = doubandata.read()

jieba.analyse.set_stop_words('ChineseStopWords.txt')
filteredwords = jieba.analyse.extract_tags(comments,topK = 200,\
                                           withWeight = True)


cloudpic = imageio.imread('cartoon.jpg')
wc = WordCloud(font_path = 'myfont.ttf',background_color = 'white',\
               max_words = 1800,mask = cloudpic,max_font_size = 120,\
               random_state = 18)

wc.generate_from_frequencies(dict(filteredwords))
wc.to_file("mywordcloud.jpg")

plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(cloudpic,cmap = plt.cm.gray)
plt.axis("off")
plt.show()

doubandata.close()


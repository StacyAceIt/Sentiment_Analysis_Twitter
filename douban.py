#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:07:08 2018

@author: yolanda7zhang
"""

import requests
from lxml import etree
import pandas as pd
from snownlp import SnowNLP
from translate import Translator

# This is the driver file which gets data from douban

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': 'll="108258"; bid=c_DEXmYxIW0; __utmc=30149280; _ga=GA1.2.1500954839.1544398087; _gid=GA1.2.1745033158.1544398095;\
 ps=y; ue="yolanda7zhangwoo@gmail.com";\
 _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1544400620%2C%22https%3A%2F%2Faccounts.douban.com%2Fsafety%2Funlock_sms%2Fresetpassword%3Fconfirmation%3D37d7daf9b9b3e034%26alias%3D%22%5D;\
 _pk_ses.100001.8cb4=*; __utma=30149280.1500954839.1544398087.1544398087.1544400623.2; __utmz=30149280.1544400623.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/safety/unlock_sms/resetpassword; \
 __utmt=1; dbcl2="155969275:Jr9qg6BDHv0"; ck=j21-; _pk_id.100001.8cb4=cd1c5d381b029a22.1544398083.2.1544400646.1544398083.; \
 ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15596; __utmb=30149280.3.10.1544400623'} 


# start = 0 to start = 480
# referred to https://zhuanlan.zhihu.com/p/42657160
datalist = []
#create a file to store data
douban = open("doubanData.txt","w+")

for i in range(0,500,20):
    try: 
        url = "https://movie.douban.com/subject/26786642/comments?start=%d&limit=20&sort=new_score&status=P" %i
        myurl = requests.get(url, cookies = cookies, headers = headers)
        myhtml = myurl.content.decode(myurl.encoding)

        treeObj = etree.HTML(myhtml)
        target = treeObj.xpath("//div[@class='comment-item']/div[@class='comment']/p/span[@class='short']/text()")
        datalist.extend(target)
    except Exception as e:
        print(e)


print(len(datalist))

for i in range(len(datalist)):
    #douban.write(str(i))
    douban.write(str(datalist[i]))
    douban.write("\n")

#print(target)

douban.close()

def getSentiment(datalist):
    sentlist = []
    for i in range(len(datalist)):
        s = SnowNLP(datalist[i])
        sentiment = s.sentiments
        sentlist.append(sentiment)
    return sentlist

def getTranslation(datalist):
    engTrans = []
    translator= Translator(from_lang = "zh",to_lang="en")
    for i in range(len(datalist)):
        translation = translator.translate(datalist[i])
        engTrans.append(translation)
    return engTrans

    

#store data to dataframe
df = pd.DataFrame(datalist, columns = ["comments"])
#create a sentiment column
df['sentiment'] = getSentiment(datalist)
df['Translation'] = getTranslation(datalist)

print(df['Translation'].head())

df.to_csv("doubanComments.csv")

#print(sentlist[:10])
#%%

df = df.sort_values(by = ['sentiment'],ascending = False)
df = df.reset_index(drop=True)

print("The summary for sentiment from Douban is \n",df['sentiment'].describe())
print("median    ",df.loc[:,'sentiment'].median())



df['sentiment'].plot.hist(alpha = 0.5)



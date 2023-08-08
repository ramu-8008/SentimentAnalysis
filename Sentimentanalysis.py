#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# In[2]:


import csv
from textblob import TextBlob


# In[30]:


# Read comments from the CSV file with the correct encoding
comments = []
sentiments = []
weight = []
dic = []


# In[31]:


with open('final_facebook_comments1.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row[2])  # Assuming the comments are in the first column


# In[32]:


comments = comments[1:]
comments


# In[33]:


# Perform sentiment analysis on each comment
for comment in comments:
    # Create a TextBlob object
    blob = TextBlob(comment)

    # Perform sentiment analysis
    sentiment = blob.sentiment.polarity

    # Interpret the sentiment polarity
    if sentiment > 0:
        sentiment_label = 'Positive'
    elif sentiment < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    sentiments.append(sentiment_label)
    weight.append(sentiment)
    dic.append((comment,sentiment_label))
    # Print the comment and its sentiment
    print('Comment:', comment)
    print('Sentiment:', sentiment_label)
    print('---')


# In[34]:


import pandas as pd
df = pd.DataFrame(dic,columns = ['comment','sentiment'])


# In[35]:


df


# In[36]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[37]:


plt.figure(figsize = (7,7))
plt.bar(range(3),[len(df[df["sentiment"]=="Positive"]),len(df[df["sentiment"]=="Neutral"]),len(df[df["sentiment"]=="Negative"])],color = ['g','b','r'])
plt.xticks(range(3),["positive","neutral",'negative'])
plt.show()


# In[39]:


plt.figure(figsize = (15,15))
plt.bar(range(40), weight[:40], color=['g' if s == "Positive" else 'r' for s in sentiments])
plt.xticks(range(40), df['comment'][1:41], rotation=30, ha='right')
plt.ylabel("Sentiment Score")
plt.title("Sentiment Analysis")
plt.show()


# In[ ]:




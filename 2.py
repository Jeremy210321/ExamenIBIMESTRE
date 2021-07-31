#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tweepy


# In[2]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[3]:



###API ########################
ckey = "rNO199RuABkS0WAoWoYXYWTDW"
csecret = "tAx0U7PrIRZCzOCvlvIodDv8lF8SMiP5ZmNSbJSPKJCkpjKD6Q"
atoken = "1418325908956532736-jy9vNbCiovMjZx5dMglni06vW9XQ2P"
asecret = "EFk5IQQBIa4WTzCm4yOBGobShr4b582RPloTzMLMMKELB"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
            print("Se guardo con éxito")
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Jeremy:IsmaelGarzon2001@localhost:5984')  #('http://115.146.93.184:5984/')
try:
    db = server.create('twittertrack')
except:
    db = server['twittertrack']
    
'''===============LOCATIONS=============='''    

# twitterStream.filter(locations=[-112.101607,40.699893,-111.739476,40.85297])   #Salt Lake City
twitterStream.filter(track=['Juegos olímpicos','olimpiadas'])
# twitterStream.filter(locations=[84.081651,27.964948,84.164813,28.023827])  #Pyeong Chang


# In[ ]:





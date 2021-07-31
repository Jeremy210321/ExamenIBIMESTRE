#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install facebook-scraper


# In[3]:


from facebook_scraper import get_posts
import couchdb
import json
import time


# In[4]:


couch=couchdb.Server('http://Jeremy:IsmaelGarzon2001@localhost:5984')
db=couch.create('olimpiadas')
db=couch['olimpiadas']
i=1
for post in get_posts('Juegos-Olimpicos-2021-102465382042543', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[9]:


db=couch.create('impfaceboo')
db=couch['impfaceboo']


# In[ ]:





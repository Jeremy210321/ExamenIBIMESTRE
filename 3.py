#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


pip install pandas


# In[27]:


#Aqui se hace la conexion de forma local a mongodb
from pymongo import MongoClient
CLIENT = MongoClient('mongodb://localhost:27017/')
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


# In[28]:


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[31]:


response = requests.get('https://www.nytimes.com/es/article/deportes-olimpiadas-2021.html')
soup = BeautifulSoup(response.content, "lxml")

Discipline=[]
Name=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]

post_discipline=soup.find_all("h2", class_="css-1aoo5yy eoo0vm40")
post_name=soup.find_all("p", class_="css-1clqwtf e6idgb70")
    
for element in post_discipline:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Discipline.append(limpio.strip())

for element in post_name:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Name.append(limpio.strip())

Atleta=[]
def listado():
    i=0
    for n in range(len(Name)):
        Atleta.append("Atleta " + str(i))
        i=i+1 
        
listado()


# In[ ]:





# In[34]:


response = requests.get('https://olympics.com/tokyo-2020/olympic-games/es/resultados/todos-los-deportes/deportistas.htm')
soup = BeautifulSoup(response.content, "lxml")

Discipline=[]
Name=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]

post_discipline=soup.find_all("span", class_="d-md-none")
post_name=soup.find_all("span", class_="d-none d-md-block")
    
for element in post_discipline:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Discipline.append(limpio.strip())

for element in post_name:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Name.append(limpio.strip())

Atleta=[]
def listado():
    i=0
    for n in range(len(Name)):
        Atleta.append("Atleta " + str(i))
        i=i+1 
        
listado()


# In[35]:


#Aqui se pasa el diccionario obtenido a DataFrame y se guarda como csv y json
Examen=pd.DataFrame({'Name':Name,'Discipline':Discipline}, index=Atleta)

#out = Ejergrupal.to_dict()
Examen.to_json('Atletas.json')
Examen.to_json('Atletas.csv')


# In[38]:


#Mediante la conexion se establece el nombre de la BD y la colección
db = CLIENT["Examen"]
Collection = db["olimpiadas"] 

#Obtiene el documento json generado anteriormente y lo carga en una variable
with open('Atletas.csv') as file: 
    file_data = json.load(file) 
      
#Comprueba si hay uno o más llaves en el json. Si hay más de uno aplica .insert_many(), 
#caso contrario ejecuta .insert_one()        
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 


# In[39]:


Examen


# In[ ]:





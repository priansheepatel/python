#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


a=pd.Series([2,3,4,5])
print(a)
#using tuple
a=pd.Series((20,30,40,50),index=(10,20,30,40))
print(a)
#using dictionary
a=pd.Series({"a":1,"b":2,"c":3})
print(a)


# In[13]:


#DATA FRAME
#(2D)
a=pd.DataFrame({"name":['a','b','c'],"marks":[90,100,110]})
print(a)
b=pd.DataFrame({"name":pd.Series(['a','b']),"marks":pd.Series([100,200])})
print(b)


# In[9]:


#IMPORT AND READ CSV
df=pd.read_csv("students.csv")
df.set_index("StudentID",inplace=True)#origanal data frame change karva!
print(df)


# In[11]:


print(df.shape)
print(df.ndim)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.values)


# In[29]:


#INDEXING AND SLICING USING LOC AND ILOC
#LOC METHOD it is a label base indexing
data={"name":['a','b','c','d','e','f'],
     "marks":[20,25,22,23,21,24],
     "bonus":[2,3,4,5,6,7],
     "city":["a1",'a2','a3','a4','a5','a6']}
df=pd.DataFrame(data)
print(df)
print(df.loc[5])
print(df.loc[5,"name"])
print(df[["name","city"]])
print(df.loc[0:2,["name","marks"]])
#ADD COLUMN
df.loc[:,"total"]=df["marks"]+df["bonus"]
print(df)
#ADD ROWS
df.loc[6]=["m",25,5,"a7",55]
print(df)


# In[34]:


#ILOC METHON index base method
print(df.iloc[0])
print(df.iloc[0:3])
#SLICING
print(df.iloc[0:3,0:2])


# In[71]:


#VIEWING DATA
#head()
#to view first 5 rows
print(df.head(3))
print("-----------------------------------------------------------")
#tail()
#to view last 5 rows
print(df.tail(3))
print("-----------------------------------------------------------")

#sample()
print(df.sample(2))
print("-----------------------------------------------------------")

#info() inspect method
print(df.info())
print("-----------------------------------------------------------")

#describe method
#df.describe(include=,exclude=,percentiles=)
print(df.describe())
print(df.describe().round(2))
print(df.describe(include="all"))
print(df.describe(exclude="object"))
print(df.describe(percentiles=[.2,.3,.4,.5]).round(2))
print("-----------------------------------------------------------")

#UNIQUE AND NUNIQUE METHOD
print(df["city"].unique())
print("-----------------------------------------------------------")

#VALUE COUNT
print(df["marks"].value_counts())
print("-----------------------------------------------------------")

#MISSING DATA HANDLING
print("-----------------------------------------------------------")

#ISNULL VALUE
print(df.isnull())
print(df.isnull().sum())
print("-----------------------------------------------------------")
#FILLINA METHOD
print(df.fillna("python"))


# In[ ]:





# In[ ]:





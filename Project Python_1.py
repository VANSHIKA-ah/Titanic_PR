#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hello World. This is my first EDA in Titanic Data")


# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


pd.read_csv("titanic.csv")


# In[29]:


titanic_data


# In[30]:


#Seeing Columns Names
titanic_data.columns


# In[31]:


#Geting information about data
titanic_data.info()


# In[32]:


titanic_data.shape


# In[33]:


#finding where values is null
titanic_data.isnull()


# In[74]:


#viewing null value using heatmap
sns.heatmap(titanic_data.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[76]:


#Droping column cabin
titanic_data.drop('Cabin',axis=1,inplace=True)


# In[77]:


#viewing null value using heatmap
sns.heatmap(titanic_data.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[38]:


#Viewing survived data using countplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=titanic_data)


# In[40]:


#viewing sex and survived data using countplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=titanic_data,palette='RdBu_r')


# In[42]:


titanic_data.head()


# In[70]:


#Viewing Passengerclass and survived data using countplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=titanic_data,palette='rainbow')


# In[49]:


titanic_data['Age'].hist(bins=30,color='r',alpha=0.4)


# In[50]:


sns.countplot(x='SibSp',data=titanic_data)


# In[51]:


plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=titanic_data,palette='winter')


# In[52]:


titanic_data[['Age','Embarked']].isnull().sum()


# In[53]:


#sum of null value from dataset
titanic_data.isnull().sum()


# In[54]:


titanic_data['Age'].value_counts()


# In[55]:


titanic_data['Age'].unique()


# In[56]:


titanic= titanic_data.fillna(method="pad")


# In[57]:


titanic['Age'].fillna(method="ffill")


# In[58]:


titanic=titanic.fillna(method='ffill')


# In[59]:


titanic.isnull().sum()


# In[60]:


titanic.fillna(method='bfill')


# In[61]:


titanic.isna()


# In[63]:


titanic.isna().sum()


# In[64]:


titanic.tail()


# In[65]:


#Viewing survived data using countplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=titanic)


# In[67]:


#Viewing sex and survived data using countplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=titanic,palette='RdBu_r')


# In[68]:


#Viewing Passengerclass and survived data using coutplot
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=titanic,palette='rainbow')


# In[69]:


titanic_data['Age'].hist(bins=30,color='b',alpha=0.4)


# In[78]:


sns.countplot(x='SibSp',data=titanic)


# In[80]:


#Viewing null value using heatmap
sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap='viridis' )


# In[84]:


plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=titanic,palette='winter')


# In[87]:


plt.plot(titanic['Age'],color='y',label='Survived',linewidth=2)


# In[88]:


plt.plot(titanic['Sex'],color='r',label='Survived',linewidth =2)


# In[90]:


plt.plot(titanic['Pclass'],color='g',label='Parch',linewidth=2)


# In[ ]:





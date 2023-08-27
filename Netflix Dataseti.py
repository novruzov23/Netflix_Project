#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv('8. Netflix Dataset.csv')


# In[3]:


df.head(100)


# In[4]:


df.isnull().any()


# In[5]:


df.notnull().sum()


# In[6]:


df.notnull().value_counts()


# In[7]:


df.notnull().any()


# In[5]:


df.isnull().sum()


# In[ ]:





# In[6]:


df.columns


# In[8]:


def data(df1):
    print('##### ndim ######')
    print(df1.ndim)
    print('##### shape ######')
    print(df1.shape)

data(df)


# In[9]:


# tekrar eden deyerler varmi 
df.duplicated()


# In[21]:


df.duplicated().value_counts()


# In[22]:


df.fillna(0, inplace=True)


# In[24]:


df.isnull().sum()


# In[25]:


df.info()


# In[26]:


df.describe().T


# In[27]:


# is there any nuul value present in any column show with heat-map
import seaborn as sns


# In[28]:


# grafik temiz olacaq. Bunun sebebi fillna() kodunun yardimi ile eksik olan deyerleri 0 lamisiq
sns.heatmap(df.isnull())


# In[34]:


# for house of cards. what is show id and who is the director of this show

df['Show_Id'].value_counts()


# In[38]:


df['Title'].isin(['House of Cards'])


# In[39]:


df['Title'].value_counts()


# In[40]:


df[df['Title'].isin(['House of Cards'])]


# In[45]:


# in which year heighest number of the tv show & movies released? show with bar graph

df.groupby(df['Category']=='Movie')['Show_Id'].count()


# In[46]:


df.groupby('Category').Category.count()


# In[118]:


df.groupby(df['Category'])['Show_Id'].count()


# In[47]:


df.groupby(df['Category']=='Movie').count()


# In[50]:


df.head(5)


# In[ ]:


# show all the movies that were weleased in year 2000 = 2000 yılında vizyona giren tüm filmleri göster


# In[56]:


df.dtypes


# In[57]:


df.info()


# In[58]:


df.columns


# In[60]:


df.head(4)


# In[74]:


df.loc[(df['Category']=='Movie') & (df['Release_Date']=='August 14, 2020')]


# In[ ]:


# show only the Title of all Shows that were released in India only = yalnızca Hindistan'da yayınlanan tüm Şovların yalnızca Başlığını göster


# In[76]:


df.loc[(df['Category']=='TV Show')  & (df['Country']=='Brazil')]


# In[77]:


# show categorisine aid olan ve Turkiyede yayinlanan show programlari
df.loc[(df['Category']=='TV Show')  & (df['Country']=='Turkey')]


# In[8]:


df['Type'].isin(['Comedies', 'Dramas'])


# In[9]:


df['Type'].isin(['Comedies', 'Dramas']).count()


# In[11]:


df['Type'].value_counts()


# In[12]:


df['Type'].isin(['Documentaries','Crime']).count()


# In[13]:


df['Type'].isin(['Documentaries','Crime'])


# In[20]:


df[(df['Category']=='Movie') &  (df['Cast']=='Erdem Yener')].count()


# In[ ]:


df


# In[78]:


df.loc[(df['Category']=='Movie') & (df['Country']=='Turkey')]


# In[80]:


# Show top 10 Directors who gave the highest number of The Shows & Movies to Netflix=Netflix'e en çok Şovlar ve Filmler veren ilk 10 Yönetmeni göster


# In[88]:


df['Description'].value_counts().head(10)


# In[ ]:


# Show all the Records, where 'Category is Movie and Types in Comediles' or Country is United Kingdom = 'Kategorinin Film ve Komedi Türleri olduğu' veya Ülkenin Birleşik Krallık olduğu tüm Kayıtları göster


# In[89]:


df[(df['Category']=='Movie') & (df['Type']=='Comedies')]


# In[93]:


df[(df['Category']=='Movie') & (df['Type']=='Comedies')| (df['Country']=='United Kingdom')]


# In[ ]:


# in how many movies/ show Tom Cruise was cast = Tom Cruise kaç filmde/dizide rol aldı?


# In[95]:


df.loc[(df['Cast']=='Tom Cruise')]


# In[100]:


df['Rating'].unique()


# In[106]:


df['Rating'].nunique()


# In[ ]:


# Netflix'te bir Filmin/Şovun maksimum süresi ne kadardır?


# In[110]:


df['Duration'].unique()


# In[111]:


df['Duration'].unique().max()


# In[119]:


df['Duration'].unique().min()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("data/linear.csv")
df.tail()


# In[7]:


fig = plt.figure()
ax = plt.axes()


# In[11]:


df1 = df[df.tipe == 'data1']
df2 = df[df.tipe == 'data2']


# In[16]:


plt.scatter(df1.X, df1.y)
plt.scatter(df2.X, df2.y)


# In[22]:


sc =sns.lmplot("X", "y", data=df, hue='tipe')


# In[27]:


sns.distplot(df.y);


# # Seaborn + Pandas

# ### Numerical

# In[28]:


df = pd.read_csv("data/cereal.csv", index_col='name')
df.head()


# ## Missing Value Visualization

# In[30]:


sns.heatmap(df.isna(), cbar=False, cmap="Blues")


# In[31]:


sns.heatmap(~df.isna(), cbar=False, cmap="Blues")


# In[32]:


plt.figure(figsize=(15, 15))
sns.heatmap(~df.isna(), cbar=False, cmap="Blues")


# In[33]:


df.dropna(inplace=True)


# ### Correlation

# In[44]:


plt.figure(figsize=(6, 6))
sns.heatmap(df.corr(), cmap='bwr', vmin=-1, vmax=1, 
            square=True, cbar=False, annot=True,
           fmt=".1f")


# ### Pairplot

# In[45]:


sns.pairplot(df)


# In[47]:


sns.pairplot(df, vars=["calories", "fat", "rating"], hue="shelf")


# In[48]:


sns.pairplot(df, vars=["calories", "fat", "rating"], hue="shelf", kind='reg')


# In[49]:


sns.jointplot("potass", "fiber", data=df)


# ## Categorical Data

# ### Persebaran

# In[50]:


sns.catplot("mfr", "rating", data=df)


# In[51]:


sns.boxplot("mfr", "rating", data=df)


# In[52]:


sns.violinplot("mfr", "rating", data=df)


# ### Frekuensi

# In[54]:


sns.catplot("mfr", data=df, kind="count")


# In[55]:


sns.countplot("mfr", data=df, hue="shelf")


# In[ ]:





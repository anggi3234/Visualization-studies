#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt


# # Inisialisasi Figure and Axes

# In[2]:


X = np.linspace(0,10,10)
y = np.sqrt(X)


# In[4]:


fig = plt.figure()
ax = plt.axes()


# In[6]:


fig = plt.figure()
ax = plt.axes()
ax.plot(X, y)


# In[9]:


fig = plt.figure(figsize=(6, 6))
ax = plt.axes()
ax.plot(X, np.sin(X))
ax.plot(X, np.cos(X))


# In[ ]:





# ## Shortcut untuk simple figure

# In[10]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X))
plt.plot(X, np.cos(X))


# ### Color Style

# In[11]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r')
plt.plot(X, np.cos(X), 'b')


# ### Line Style

# In[17]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r--') #Red dashed line
plt.plot(X, np.cos(X), 'c+-') #Blue oval


# ```
#     'b'    #Blue line, marker default
#     'ro'   #Red circle line
#     'g-'   #Default color, dashed line
#     'k^'   #Black triangle
#     'c+-'  #Cyan with plus marked with solid line
# ```    

# ### Axis Limit

# In[19]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r')
plt.plot(X, np.cos(X), 'b')
plt.xlim(0,15)
plt.ylim(-2,2)


# In[20]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r')
plt.plot(X, np.cos(X), 'b')
plt.axis('equal')


# # Back to non-shortcut

# In[22]:


plt.figure(figsize=(6,6))
plt.plot(X, np.sin(X), 'r--', linewidth=3)
plt.plot(X, np.cos(X), 'bo', markersize=5)
plt.xlim(0,15)
plt.ylim(-2,2)

plt.title("2 fungsi trigonometrik")
plt.xlabel("X")
plt.ylabel("y")


# In[24]:


fig = plt.figure(figsize=(6,6))

ax =plt.axes()
ax.plot(X, np.sin(X), 'r--', linewidth=3)
ax.plot(X, np.cos(X), 'bo', markersize=5)

ax.set(xlim=(0,15), ylim=(-2,2), title="2 fungsi trigonometrik",
                                    xlabel="X",
                                    ylabel="y")


# In[25]:


fig = plt.figure(figsize=(6,6))

ax =plt.axes()
ax.plot(X, np.sin(X), 'r--', linewidth=3, label="sin(x)")
ax.plot(X, np.cos(X), 'bo', markersize=5, label='cos(x)')

ax.set(xlim=(0,15), ylim=(-2,2), title="2 fungsi trigonometrik",
                                    xlabel="X",
                                    ylabel="y")
ax.legend()


# # Scatter Plot

# In[30]:


sc = pd.read_csv("data/circle_data.csv", sep=';')


# In[32]:


sc.head()


# In[34]:


plt.scatter(sc.x, sc.y)
plt.axis('equal')


# In[36]:


plt.scatter(sc.x, sc.y, c='r', s=30)
plt.axis('equal')


# In[37]:


plt.scatter(sc.x, sc.y, c=sc.radius, s=30, cmap='seismic')
plt.axis('equal')


# In[39]:


plt.scatter(sc.x, sc.y, c=sc.radius, s=sc.radius*50, cmap='viridis')
plt.axis('equal')


# # Historgram

# In[40]:


numbers = np.random.rand(10000)
plt.hist(numbers, bins=25)


# In[41]:


numbers = np.random.rand(10000)
plt.hist(numbers, bins=25);


# In[42]:


numbers = np.random.randn(10000)
plt.hist(numbers, bins=25);


# In[43]:


numbers = np.random.randn(10000)
plt.hist(numbers, bins=25, density=1);


# In[44]:


numbers = np.random.randn(10000)
plt.hist(numbers, bins=25, density=1, cumulative=True);


# # SubPlot
# One canvas for more than one coordinates

# ### MATLAB Style

# In[48]:


plt.subplot(2, 2, 1)
plt.scatter(sc.x, sc.y, c='r', s=30)
plt.axis('equal')

plt.subplot(2, 2, 2)
plt.scatter(sc.x, sc.y, c=sc.radius, s=sc.radius*50, cmap='viridis')
plt.axis('equal')

plt.subplot(2, 2, 4)
plt.scatter(sc.x, sc.y, c=sc.radius, s=30, cmap='seismic')
plt.axis('equal');


# ## Matplotlib style

# In[52]:


fig, ax = plt.subplots(2, 3)
ax[0,0].scatter(sc.x, sc.y, c='r', s=30)
ax[0,2].scatter(sc.x, sc.y, c='r', s=30)
ax[1,1].scatter(sc.x, sc.y, c='r', s=30)
ax[1,2].scatter(sc.x, sc.y, c='r', s=30);


# In[54]:


fig, ax = plt.subplots(2, 3, figsize=(16, 11))
ax[0,0].scatter(sc.x, sc.y, c='r', s=30)
ax[0,2].scatter(sc.x, sc.y, c='r', s=30)
ax[1,1].scatter(sc.x, sc.y, c='r', s=30)
ax[1,2].scatter(sc.x, sc.y, c='r', s=30);


# In[55]:


fig, ax = plt.subplots(2, 3, figsize=(16, 11), sharex=True,
                      sharey=True)
ax[0,0].scatter(sc.x, sc.y, c='r', s=30)
ax[0,2].scatter(sc.x, sc.y, c='r', s=30)
ax[1,1].scatter(sc.x, sc.y, c='r', s=30)
ax[1,2].scatter(sc.x, sc.y, c='r', s=30);


# In[ ]:





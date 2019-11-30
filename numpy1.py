#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[11]:


my_list = [1,2,3,4,5,6,7,8,9,0] 


# In[14]:


arr = np.array(my_list)


# In[15]:


arr


# In[16]:


my_matr = [[1,2,3],[4,5,6],[7,8,9]]


# In[17]:


np.array(my_matr)


# In[18]:


np.arange(0,5)


# In[19]:


np.arange(0,20,3)


# In[22]:


np.zeros(3)


# In[23]:


np.ones((4,6))


# In[24]:


np.linspace(0,10,5)


# In[25]:


np.linspace(0,5,10)


# In[26]:


np.eye(3)


# In[27]:


np.random.rand(6)


# In[28]:


np.random.rand(6)


# In[30]:


np.random.rand(2,3)


# In[31]:


np.random.randint(40,60)


# In[32]:


np.random.randint(40,60)


# In[33]:


np.random.randint(1,50,5)


# In[34]:


arr1 = np.arange(10)


# In[35]:


arr1


# In[36]:


random_arr = np.random.randint(0,20,5)


# In[37]:


random_arr


# In[38]:


arr1.reshape(2,5)


# In[39]:


random_arr


# In[40]:


random_arr.max()


# In[41]:


random_arr.min()


# In[42]:


random_arr.argmax()


# In[43]:


random_arr.argmin()


# In[47]:


arr1 = arr1.reshape(5,2)


# In[48]:


arr1


# In[50]:


arr1.shape


# In[51]:


arr.dtype


# In[52]:


arr1.dtype


# In[53]:


from numpy.random import randint


# In[54]:


randint(1,50)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3], dtype='int32')
print(a)


# In[3]:


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
b


# In[4]:


# Get Dimension
a.ndim


# In[5]:


# Get Shape
b.shape


# In[6]:


# Get Type
a.dtype


# In[7]:


# Get Size
a.itemsize


# In[8]:


# Get total size
a.nbytes


# In[9]:


# Get number of elements
a.size


# In[10]:


#another way to get total size
a.size * a.itemsize


# In[11]:


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)


# In[12]:


# Get a specific element [r, c]
a[1, 5]


# In[13]:


# Get a specific row 
a[0, :]


# In[14]:


# Get a specific column
a[:, 2]


# In[15]:


# Getting a little more fancy [startindex:endindex:stepsize] end index is exclusive, ie enter 1 extra
a[0, 1:6:2]


# In[16]:


# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]


# In[17]:


# changing values of elements
a[1,5] = 20

a[:,2] = [1,2]
print(a)


# In[18]:


#3-D array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[19]:


# Get specific element (work outside in)
b[0,1,1]


# In[20]:


# All 0s matrix
np.zeros((2,3))


# In[21]:


# All 1s matrix
np.ones((4,2,2), dtype='int32')


# In[22]:


# Any other number
np.full((2,2), 99)


# In[23]:


# Any other number (full_like- dimensions of any other array, a in this example)
np.full_like(a, 4)


# In[26]:


# Random decimal numbers
np.random.rand(4,2)


# In[27]:


# Random Integer values
np.random.randint(-4,8, size=(3,3))


# In[28]:


# The identity matrix
np.identity(5)


# In[29]:


# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)


# In[30]:


output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z 
# can use -1 instead of 4
print(output)


# ##### Be careful when copying arrays !!!
# 

# In[31]:


# WRONG METHOD AS NO COPY OF a is created nad the changes in be are reflected in a.
a = np.array([1,2,3])
b = a
b[0] = 100

print(a)


# In[32]:


# RIGHT METHOD
a = np.array([1,2,3])
b = a.copy()
b[0] = 100

print(a)


# ### MATHEMATICS
# 

# In[33]:


a = np.array([1,2,3,4])
print(a)


# In[34]:


a + 2


# In[35]:


a - 2


# In[36]:


a * 2


# In[37]:


a / 2


# In[38]:


a ** 2


# In[39]:


# Take the sine
np.sin(a)


# ### Linear Algebra
# 

# In[40]:


a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b)


# In[41]:


# Find the determinant
c = np.identity(3)
np.linalg.det(c)


# ### Statistics

# In[42]:


stats = np.array([[1,2,3],[4,5,6]])
stats


# In[43]:


np.min(stats)


# In[44]:


np.max(stats)


# In[47]:


np.max(stats,axis=1)


# In[45]:


np.sum(stats)


# In[48]:


np.sum(stats, axis= 0)


# In[49]:


np.sum(stats, axis= 1)


# ### Reorganizing Arrays

# In[50]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)


# In[51]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,3))
print(after)


# In[52]:


# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2])


# In[53]:


# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])


# In[54]:


# Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))


# ### Miscellaneous
# 
# #### Load Data from File

# In[57]:


filedata = np.genfromtxt("N:\YY\data.txt", delimiter=',')
filedata = filedata.astype('int32')
print(filedata)


# In[62]:


filedata > 50


# In[61]:


filedata[filedata > 50] 


# In[63]:


((filedata > 50) & (filedata < 100))


# In[60]:


# you can index with a list in an array
a = np.array([1,2,3,4,5,6,7,8,9])

a[[1,2,8]]


# In[ ]:





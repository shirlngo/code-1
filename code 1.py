#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prevalence
population = int(input("Population: "))
existingcases = int(input("Existing cases: "))
prevalence = existingcases / population
print(prevalence)
print(prevalence*100000)


# In[3]:


# incidence
newcases = int(input("New cases: "))
incidence = newcases / population
print(incidence)
print(incidence * 100000)


# In[4]:


# mortality rate
dead = int(input("Number of those who died: "))
segment = int(input("Number of those who had the disease: "))
mortalityrate = dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)


# In[5]:


# years of potential life loss
lifeexpectancy = 77
ages = [64, 74]
print(lifeexpectancy - ages[0])
print(lifeexpectancy - ages[1])


# In[6]:


lifelost = [13,3]
yppl = sum(lifelost) / len(lifelost)
print(yppl)


# In[ ]:





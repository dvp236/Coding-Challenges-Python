
# coding: utf-8

# In[1]:

print "Swaminarayan"


# In[8]:

#for given number sum all of them:
#We will use recursion here 

def sum(n):
    if n<=9:
        return n
    else:
        return n%10 + sum(n/10)
        


# In[9]:

sum(1234)


# In[ ]:




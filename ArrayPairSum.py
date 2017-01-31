
# coding: utf-8

# In[1]:

print "Swaminarayan!"


# In[37]:

def getPairs(array,number):
    
    if len(array) <= 2:
        return
    
    seen = set()
    output = set()
    
    for item in array:
        target = number - item
        #if can not make a pair, add it to set for later use
        if target not in seen:
            seen.add(item)
        
        else:
            output.add((min(target,item),max(target,item)))
                       
    return output



# In[41]:

result = getPairs([1,2,3,6,5,4],7)
print "\n".join(map(str,list(result)))


# In[ ]:




# In[ ]:





# coding: utf-8

# In[1]:

print "Jsn _/\_"


# In[2]:

def rev1(s):
    return " ".join(reversed(s.split()))

def rev2(s):
    return " ".join(s.split()[::-1])


# In[8]:

print rev1('patel dharmik am i  ')


# In[6]:

print rev2("i am dharmik     patel")


# In[9]:

#manually 
#since we have to ignore excess spaces
def rev3(s):
    
    words = []
    spaces = [' ']
    i = 0
    
    while(i < len(s)):
        if s[i] not in spaces:
            word_start = i
            while i < len(s) and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1
        
    return " ".join(reversed(words))
            
    


# In[10]:

print rev2("i am dharmik     patel")


# In[ ]:




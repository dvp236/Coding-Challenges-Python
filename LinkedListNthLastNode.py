
# coding: utf-8

# In[1]:

print "Swaminarayan !"


# In[ ]:

#depends on implementation of linked list.
#in a normal implementation 
def getNthLast(head,n):
    #here we take 2 pointers. the right pointer and left pointer will have difference of n 
    #thus when right reached the end of linked list, left pointer will be n node ahead.
    left = head
    right = head
    
    i = 0
    while i<n:
        right = right.getnext()
    
    while right.getnext != None:
        right = right.getnext()
        left = left.getnext()
        
    return left
    


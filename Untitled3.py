#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
row_num=num+num//2+2
col_num=num+2
star_handler,con=0,0
if num%2!=0:
    for i in range(row_num):
        #It,s for t make T shape 
        for j in range(col_num):
            if i<=1: 
                if j<=num-1:  print("*",end="")      
                else:  print(" ",end='')     
            elif i>1 and i<num+1:
                if j==num//2 : print("*",end='')    
                else :  print(" ",end='')
            elif i>1 and i==num+1:
                if j>=num//2 : print("*",end='')    
                else :  print(" ",end='')
            else : print(" ",end='')
       #for trignle makeing
        if i>num//2+1:
            if con<=num//2 : star_handler+=1    
            else : star_handler-=1
            con+=1
            for j in range(star_handler) : print("*",end='')
              
        print()


# In[ ]:





# In[ ]:





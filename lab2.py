#!/usr/bin/env python
# coding: utf-8

# In[2]:


def words():
            s = input() 
            first_word = s[:s.find(' ')] 
            second_word = s[s.find(' ') + 1 : ] 
            print(second_word + ' ' + first_word)


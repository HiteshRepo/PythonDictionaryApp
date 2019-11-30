# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 14:08:39 2019

@author: Hitesh Pattanayak
"""

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process

print(fuzz.ratio('geeksforgeeks', 'geeksgeeks')) #87 - looks for exact match

print(fuzz.partial_ratio("geeks for geeks", "geeks for geeks!")) #100 looks for contains [partial match]
  
print(fuzz.partial_ratio("geeks for geeks", "geeks geeks")) #64

print(fuzz.token_sort_ratio("geeks for geeks", "for geeks geeks")) #100 - This gives 100 as every word is same, irrespective of the position 

query = 'geeks for geeks'
choices = ['geek for geek', 'geek geek', 'g. for geeks']  
   
# Get a list of matches ordered by score, default limit to 5 
print(process.extract(query, choices) ) #[('geeks geeks', 95), ('g. for geeks', 95), ('geek for geek', 93)] 
   
# If we want only the top one 
print(process.extractOne(query, choices)) #('geeks geeks', 95) )
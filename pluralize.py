# -*- coding: utf-8 -*-

# pluralize words in a dictionary. Produces some noise (plurelized form of already plural words)

import os,sys
reload(sys)
sys.setdefaultencoding('utf8') # quick and dirty fix to be able to redirect into file


import pattern.en 

DIC_PATH = 'bigdict.txt'
OUT_DIC_PATH = 'bigdict_pluralized.txt'

# read words
with open(DIC_PATH) as f:
    words_list = [p.rstrip('\n').strip(' ') for p in f.readlines()]


pluralized_words_list = []
#create new list that includes pluralized forms
for word in words_list:
    pluralized_words_list.append(word)
    pluralized_words_list.append(pattern.en.pluralize(word))
    
with open(OUT_DIC_PATH, 'w') as f2:
    for word in pluralized_words_list:
        print>>f2, word
        
print('done')
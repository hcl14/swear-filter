# -*- coding: utf-8 -*-



import os,sys
reload(sys)
sys.setdefaultencoding('utf8') # quick and dirty fix to be able to redirect into file

import re 

# load dictionary to list -------------------------

parentpath= os.path.dirname(os.path.realpath(__file__))

DIC_PATH=os.path.join(parentpath,'bigdict.txt')

with open(DIC_PATH) as f:
    words_list = [p.rstrip('\n').strip(' ') for p in f.readlines()]
    


#https://stackoverflow.com/questions/15658187/replace-all-words-from-word-list-with-another-string-in-python

big_regex = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, words_list))) # replaces words only
big_regex_substr = re.compile('|'.join(map(re.escape, words_list))) # substrings

# -------------------------------------------------    
    
generic_replacement = ' ' # one space


def clean_string(utfstring, substr=True): # just plainly remove everything from string
    
    if utfstring is None:
        return ""
    
    global generic_replacement
    
    if substr:
        return big_regex_substr.sub(generic_replacement,utfstring)
    else:
        return big_regex.sub(generic_replacement,utfstring)


def mark_string(utfstring, substr=True): # marks the suspicious subtext in the string, overlap is not possible
    
    if utfstring is None:
        return []
    
    if substr:
        res = big_regex_substr.finditer(utfstring)
    else:
        res = big_regex.finditer(utfstring)

    #finditer - Return an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern in string. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result unless they touch the beginning of another match.
    
    if res is not None:    
        return [{utfstring[m.start(0):m.end(0)]: (m.start(0), m.end(0))} for m in res]
    else: 
        return []
 

# Examples:

#print(mark_string("Some,shitty!shitty fucking text for real bitches. Yeah, asshole"))
    
#print(mark_string("Everything is good here"))

#print(clean_string('shit'))

#print(mark_string("shittyass"))

#print(mark_string("shit023 from 002ass"))
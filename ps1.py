###### this is the first .py file ###########
#!/bin/python

import sys
import collections
print sys.argv[1:] #input from terminal
dict = {}

for letter in sys.argv[1:]:
	if letter not in dict.keys(): #checking valid input 
		dict[letter] = 1
		
	else: 
		dict[letter] = dict[letter] + 1 #checking existence of each word  
print dict

def top3words(dict):
    freq = collections.Counter(dict)
    return [elem for elem, _ in freq.most_common(3)] #calculating frequency of word

x = top3words(dict)
print x

list= top3words(dict)
print list
word1=list[0]
b= ''.join(sorted(word1))
print b

word2=list[1]
w= ''.join(sorted(word2))
print w
word3=list[2]
f= ''.join(sorted(word3))
print f


####### write your code here ##########

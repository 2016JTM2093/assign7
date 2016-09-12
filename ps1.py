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
list.sort()
str1=list[0]
for letter in str1
	if str1[0] < str1[1]: #swapping according to letters in dictionary
		temp=str1[1]
		str1[0]=str1[0]
		str1[0]=temp
	else:
		continue
print list[0]
####### write your code here ##########

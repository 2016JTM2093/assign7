###### this is the third .py file ###########
#!/bin/python
import ast
dict1 = {'place': 'IIT roorkee', 'city': 'Roorkee', 'state': 'Uttarakhand'}
dict2 = {'place': 'IIT delhi', 'city': 'delhi', 'state': 'new delhi'}
dict3 = {'place': 'IIT bombay', 'city': 'mumbai', 'state': 'maharashtra'}
print dict1
print dict2
print dict3


def add(dict1,dict2,dict3):       #define function for adding a field in dictionary
    dict1.update({'name': 'pooja'})
    dict2.update({'name': 'manpriya'})
    dict3.update({'name': 'rohit'})
    print dict1
    print dict2
    print dict3
    return
####### write your code here ##########

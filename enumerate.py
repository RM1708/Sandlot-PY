
#From: https://ide.geeksforgeeks.org/wcGsr8WWPc

# Python program to illustrate
# enumerate function in loops
l1 = ["eat","sleep","repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)
print
# changing index and printing separately
for count,ele in enumerate(l1,100):
	print (count,ele)

l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("\n", list(enumerate(l1)))
print (list(obj1),"\n")
#[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

print ("Return type:",type(obj1),"\n")
#Return type: <class 'enumerate'>

# changing start index to 2 from 0
print (list(enumerate(s1,2)))
print (list(obj2))
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

print ("Return type:",type(obj2),"\n")
#Return type: <class 'enumerate'>

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

#(0, 'eat')
#(1, 'sleep')
#(2, 'repeat')
print()

for ndx, ele in enumerate(l1):
    print ("Index: {}, Elem: {}".format(ndx, ele))

print()

# changing index and printing separately
for count,ele in enumerate(l1,100):
    print ("Count: {}, Elem: {}".format(count,ele))

#100 eat
#101 sleep
#102 repeat


####################################################
'''
Python 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> # Python program to illustrate
... # enumerate function
... 
>>> l1 = ["eat","sleep","repeat"]
>>> s1 = "geek"
>>> 
>>> # creating enumerate objects
... obj1 = enumerate(l1)
>>> obj2 = enumerate(s1)

>>> print (list(enumerate(l1)))
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

>>> print ("Return type:",type(obj1))
Return type: <class 'enumerate'>

>>> # changing start index to 2 from 0
... print (list(enumerate(s1,2)))
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

>>> print ("Return type:",type(obj2))
Return type: <class 'enumerate'>

>>> # printing the tuples in object directly
... for ele in enumerate(l1):
...     print (ele)
... 
(0, 'eat')
(1, 'sleep')
(2, 'repeat')
>>> print()

>>> # changing index and printing separately
... for count,ele in enumerate(l1,100):
...     print (count,ele)
... 
100 eat
101 sleep
102 repeat
>>> 
'''

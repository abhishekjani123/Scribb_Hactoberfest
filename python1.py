# -*- coding: utf-8 -*-
"""Python_0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wrQVWPaKbELQa-HqcRCxgwlfM4cr2vZ0

**python class (Beginning)**
jai shree Ganesh
"""

print("hello world")

"""**LISTS**"""

x= [4,34,2,22,45,13]
x
print(x)

a= ["hello",[4,5,5,6,34,7.8]]
print(a)
print(a[1])
print(a[0][3])
print(a[1][4])

A= [3,4,2,2,2.2]
type(A)
A.

b= [2,2,3,9,5,6,12,14]
print(b)
b.append([22,44,55,66])
print(b)

print(b.copy())
b.count(2)

c=[9,7,5,3,1,21]
c.extend([22,44,55,66])
print(c)
c.insert(3,.90)
print(c)

c.remove(9)
c.sort()
print(c)
c.reverse()
print(c)

max(c)
min(c)
del c[4:]
print(c)
sum(c[1:3])

lis=[1,2,3,4,5,6]
lis[2]= 99
print(lis)
len(lis)

"""TUPLES AND SETS"""

tup= (34,44,2,5,33)
print(tup)
type(tup)
tup.index(5)

sets = {2,2,2,45,76,88,94}
print(sets)
sets.add(77)
sets

"""DICTIONARY"""

data = {2:'good',4:'bad',"hi":'money'}
print(data)
print(data[2])
print(data.get(1))

b = [2,20,3,9,5,12] 
d = [4,34,2,22,45,13] 
h = dict(zip(b,d))
h
data.values()

a=8
id(a)
b=7
id(b)

num = 8+3j
print(num)
type(num)
a= 4
x=3
print(complex (a,x))

"""RANGE"""

print(range(0,40))
print(list(range(10,80,5)))

"""OPERATORS"""

a,b,c= 3,4,5
print(c*8)
not (a>=3 or b==9)

bin(5)
print(bin(5))
print(hex(5))
print(oct(5))
0b101

f,h,km=  50,40,[2,3,4,4,0]
print(f,h,km)
print(km)

"""SWAPING VARIABLES"""

x=3
y=4
x=y
c=3
y=c
print(x,y)

x=3
y=4
x,y=y,x
print(x,y)

~12
~20

print(12|13)  #or use
print(12&13)  #and use
print(12^13)  # ex-or
print(10<<2)  # left shift
10>>2         # right shift

import math as m
print(m.pow(2,3))



print("hi subham")

"""ARRAY"""


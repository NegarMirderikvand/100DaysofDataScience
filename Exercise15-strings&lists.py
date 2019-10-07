# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:26:33 2019

@author: Negar Mirderikvand
Days of 15 

Strings
"""
A="Hello"
B="Guys"
print(A+B)
print (A+" "+B)
print(A[0])
print(B[:2])
g=A[0:4].capitalize()
print(A.count('P',1,))
f=A.find('o')
e=A.lower()
d=A.upper()
c=A.split(sep=".")
findx=A[A.find('o'):]
print ("*".join(A))
isal=A.isalpha()
p=A.center(10,"*")
A.replace("H","HH")

"""
lists
"""
lst1=['machine','IE','IOE']
lst1[1]="ccc"

lst2=[2,'dddd',[4,3]]
lst3=lst1+lst2
len(lst1)
lst3.append(['l',3])
lst3.count('4')
lst2.pop(2)
lst1.index('ccc')
lst1.sort(reverse=True)
lst3.remove(2)
lst3.insert(2,"Succeed")
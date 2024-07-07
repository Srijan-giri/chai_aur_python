# ***  some important codes ***


"""
>>> a=3
>>> a='chaiaurcode'
>>> a=3.14
>>> a=5
>>> b=2
>>> a
5
>>> b
2
>>> a=a+3
>>> a
8
>>> myListOne=[1,2,3]
>>> myListTwo=myListOne
>>> myListTwo
[1, 2, 3]
>>> myListOne='chai'
>>> myListTwo        
[1, 2, 3]
>>> myListOne           
'chai'
>>> myListOne=[1,2,3]   
>>> myListTwo
[1, 2, 3]
>>> myListOne       
[1, 2, 3]
>>> myListOne[0]=33
>>> myListOne       
[33, 2, 3]
>>> myListTwo 
[1, 2, 3]
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]
>>> p1=[1,2,3]
>>> p2=p1
>>> p1[0]=44
>>> p1
[44, 2, 3]
>>> p2
[44, 2, 3]
>>> p2=[44,2,3]
>>> p1[0]=55
>>> p1
[55, 2, 3]
>>> p2
[44, 2, 3]
>>> h1=[1,2,3]
>>> h2=h1[:]
>>> h2
[1, 2, 3]
>>> h1
[1, 2, 3]
>>> h1[0]=55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]
>>> # h1[:] means copy of h1
>>> import copy
>>> h2=copy.copy(h1)
>>> h2
[55, 2, 3]
>>> h1
[55, 2, 3]
>>> h1[0]=65
>>> h1
[65, 2, 3]
>>> h2
[55, 2, 3]
>>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3]
>>> m==n
True
>>> m is n
False
>>> 3 is checks memory reference , it checks the same object or not
  File "<stdin>", line 1
    3 is checks memory reference , it checks the same object or not
                ^^^^^^
SyntaxError: invalid syntax
>>> #3 is checks memory reference , it checks the same object or not

"""


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the values are the same
print(a is b)  # False, because they are not the same object in memory


a = [1, 2, 3]
b = a

print(a == b)  # True, because the values are the same
print(a is b)  # True, because they are the same object in memory

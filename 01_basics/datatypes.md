# Object Type / Data Types


- Number : 1234,3.14,3+4j,0b111, Decimal(), Fraction()

- String : "Hello World", 'Hello World', """Hello World"""

- List : [1,[2,'three'],4.5],list(range(10))

- Tuple : (1,'spam',4,'U'),tuple('spam'),namedtuple

- Dictionary : {'food':'spam','taste':'yum'}.dict{hours=10}

- Set : set('abc'),{'a','b','c'}

- File : open('eggs.txt'),open(r'C:\ham.bin','wb')

- Boolean : True , False

- None : None

- Functions, modules, classes

- Advanced: Decorators, Genarators, Iterators, MetaProgramming


***** Terminal Programs Overview ******



Srijan@Srijan MINGW64 /e/Python_Tutorial
$ python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+2
4
>>> 2**100
1267650600228229401496703205376
>>> 2.5*2
5.0
>>> 12+12
24
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.0956446804845984
>>> random.choice([1,2,3,4,5])
4
>>> random.choice([1,2,3,4,5])
3
>>> random.choice([1,2,3,4,5])
4
>>> random.choice([1,2,3,4,5])
2
>>> random.choice([1,2,3,4,5])
1
>>> random.choice([1,2,3,4,5])
5
>>> random.choice([1,2,3,4,5])
2
>>> username="chaiaurcode"
>>> len(username)
11
>>> username[0]
'c'
>>> username[5]
'u'
>>> username[0]='A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> username[0]     
'c'
>>> username[-1]
'e'
>>> username[-2]
'd'
>>> username[1:3] 
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']        
>>> mylist=[123,"chai",3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)\
... cc
  File "<stdin>", line 2
    cc
    ^^
SyntaxError: invalid syntax
>>> len(mylist) 
3
>>> mylist[0]
123
>>> mylist[-1]
3.14
>>> myD={'one':'lemon','two':'ginger','comic':'nagraj'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'comic': 'nagraj'}
>>> id(myD)
2901243097792
>>> type(myD)
<class 'dict'>
>>> myD['comic']
'nagraj'
>>> myD['comics']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'comics'
>>> myTup=(1,2,40
... ^Z^Z^Z

  File "<stdin>", line 1
    myTup=(1,2,40
          ^
SyntaxError: '(' was never closed
>>> myTup=(1,2,4)
>>> myTup
(1, 2, 4)
>>> myTup[0]
1
>>> len(myTup)
3
>>> myTup[0]=5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> myTup
(1, 2, 4)
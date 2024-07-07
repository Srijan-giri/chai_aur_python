print("chai aur python")


def chai(n):
    print(n)


chai(10)
chai("lemon tea")

chai_one="lemon tea"
chai_two="ginger tea"
chai_three="masala tea"


# ? Python Shell

# >>> print('chai')
# chai
# >>> 2+2
# 4
# >>> "chai"+4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> "chai"*4  
# 'chaichaichaichai'
# >>> score=100
# >>> score
# 100
# >>> tea
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tea' is not defined
# >>> import os
# >>> os.getcwd()
# 'E:\\Python_Tutorial\\01_basics'
# >>> for c in "chai":
# ... print(c)
#   File "<stdin>", line 2
#     print(c)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for c in "chai":
# ...     print(c)
# ...
# c
# h
# a
# i
# >>> import sys
# >>> sys.platform 
# 'win32'
# >>> import hello_chai
# chai aur python
# 10
# lemon tea
# >>> hello_chai.chai("mint chai")
# mint chai
# >>> hello_chai.chai_one         
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'hello_chai' has no attribute 'chai_one'
# >>> from importlib from reload
#   File "<stdin>", line 1
#     from importlib from reload
#                    ^^^^
# SyntaxError: invalid syntax
# >>> from importlib import  reload
# >>> reload(hello_chai)
# chai aur python
# 10
# lemon tea
# <module 'hello_chai' from 'E:\\Python_Tutorial\\01_basics\\hello_chai.py'>
# >>> hello_chai.chai_one           
# 'lemon tea'
# >>>

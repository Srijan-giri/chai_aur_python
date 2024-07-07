x=2
y=3
z=4

print(x+y+z)
print(x-y-z)

print(x/y)
print(z%x)

print(x*y)
print(x**y)

print(z/x) #^ float division
print(z//x) #^ int division


print(x+y*z) #? 1) y*z  2) x+y*z  => BODMAS Rule

print(40+2.23)

# print('hirtesh'+3)

print(int(2.23))

print(float(2))

print('chai'+'code')

print(bool(0))
print(bool(1))

print(x,y,z)

print(1/3.0)

print(repr('chai'))

print(str('chai'))

print('chai')

#! difference between repr vs str vs normal print


print(1<2)

print(5.0==5.0)

print(4.0 != 5.0)

print(5.0==5)

print(x,y,z)

print(x<y<z)

print(x<y and y<z) #^ True and True = True
print(x < y and y > z)  # ^ True and False = False


print(1==2<3) #? False

print(1==2 and 2<3)

print(1==True)

print(1 == (2 < 3)) #? True



#* *** Math Library ***

import math

print(math.floor(3.5))
print(math.floor(-3.5))
print(math.floor(3.9))

print(math.trunc(2.8))
print(math.trunc(-2.8))

print(math.ceil(2.4))
print(math.sqrt(25))
print(math.pow(2,3))
print(math.lcm(2,3,4))



#**********

print(2+1j)
print(2+1j+3)
print((2+1j)*3)


#**********

print(0o20)
print(0xFF)
print(0b1000)


print(oct(64))
print(hex(255))
print(bin(7))

print(int('64',16))
print(int('111',2))

#******

#? Bitwise Operator

x=1
print(x<<2)
print(float(x>>2))
print(float(2>>1))
print(2<<3)
print(x|2)
print(x&2)
print(x^2)


#****

#^ random

import random
print(random.randint(1,10))
print(random.random())

print(math.floor(random.random()*10)+1)

l1=['lemon','masala','ginger','mint']

print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))

random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)


#******

from decimal import Decimal

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))


from fractions import Fraction

myFra = Fraction(2,7)
print(myFra)

#*******

setone = {1,2,3,4}
print(setone & {1,3,7})
print(setone | {1,3,7})
print(setone - {1,3})

print(setone - {1,2,3,4}) #? set() ==> empty set

print(type({})) #? Dictionary

print(type(set())) #? Set

#******

#^ Boolean

print(type(True))

print(True==1)
print(False==0)

print(True is 1)  #False => different object reference

print(True+4)





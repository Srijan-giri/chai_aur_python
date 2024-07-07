# 8. Prime Number Checker
# Problem: Check if a number is prime.
import math
num = int(input("Enter the number: "))

sqrt = int(math.sqrt(num))
isPrime = True

if num==0 or num==1:
    print("Not Prime")

for i in range(2,sqrt+1):
    if num%i==0:
        isPrime=False
        break

if isPrime:
    print(num," is prime")
else:
    print(num," is not prime")
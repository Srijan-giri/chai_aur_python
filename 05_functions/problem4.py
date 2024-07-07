# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stats(radius):
    print('hi')
    area =math.ceil((math.pi*(radius**2))*100)/100
    circumference = math.ceil((2*math.pi*radius)*100)/100

    return area,circumference

a,c = circle_stats(3)

print("Area: ",a,"Circumference: ",c)
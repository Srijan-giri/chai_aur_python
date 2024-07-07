# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="shaktiman",power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman",power="lazer",enemy="Dr. Jackaal")


def print_sum_objects(**kwargs):
    for key,args in kwargs.items():
        print(f"{key}:{sum(args)}")


print_sum_objects(obj1=(1,2,3,4,5),obj2=[1,2,3,4,5,6])

username = "chaiaurcode"

# ? {} ==> Scopes


def func():
    # username="chai"
    print(username)
    # ? if username not present in func() then print chaiaurcode
    # ? if username="chai" is present in func() then print chai


print(username)
func()

x = 99


def func2(y):
    z = x + y
    return z


result = func2(1)
print("func2: ", result)


"""
def func3():
    global x
    x=12

func3()
print("func3: ", x)

"""


def f1():
    # x=88
    x = 88

    def f2():
        print(x)

    return f2


myresult = f1()
print(myresult)
myresult()


def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f=chaicoder(2)
g=chaicoder(3)

print(f) #! print function reference as well as the reference of  num(2)  
print(g)  #! print function reference as well as the reference of  num(3)

print(f(2)) #^ 4
print(g(3)) #^ 27

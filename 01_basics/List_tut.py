# * List is mutable

tea_varities=["Black","Green","Oolong","White"]
print(tea_varities)

print(tea_varities[0])
print(tea_varities[1])

print(tea_varities[:])
print(tea_varities[0:3])
print(tea_varities[2:])
print(tea_varities[-1::-1])


tea_varities[3]="Herbal"
print(tea_varities)


tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities[1:2])
tea_varities[1:2]=["Lemon"]
print(tea_varities[1:3])
tea_varities[1:3]=["Green","Masala"]
print(tea_varities)
print(tea_varities[1:1])
tea_varities[1:1]=["test","test"]
print(tea_varities)
print(tea_varities[1:2])
print(tea_varities[1:3])

tea_varities[1:3]=[]
print(tea_varities)

tea_varities = ["Black", "Green", "Oolong", "White"]

for tea in tea_varities:
    print(tea,end="-")

tea_varities = ["Black", "Green", "Masala", "White"]

if "Oolong" in tea_varities:
    print("I have Oolong tea")

print()

tea_varities.append("Oolong")
print(tea_varities)

if "Oolong" in tea_varities:
    print("I have Oolong tea")

print(tea_varities.pop())
print(tea_varities)

tea_varities.remove("Green")
print(tea_varities)

tea_varities.insert(1,"Green")
print(tea_varities)


tea_varities_copy=tea_varities.copy()

print(tea_varities_copy)
print(tea_varities is tea_varities_copy)

tea_varities_copy.append("Lemon")
print(tea_varities_copy)

squared_nums=[x**2 for x in range(10)]
print(squared_nums)

cube_num=[x**3 for x in range(1,6)]
print(cube_num)

my_set = {1, 2, 2, 3, 3, 4, 5, 5}
print(my_set)

s = {}
print(type(s))
s = set()
print(type(s))

chai_type = {"masala", "lemon", "ginger"}
print(chai_type)

for chai in chai_type:
    print(chai, end="-")
print()

chai_type.add("Oolong")
print(chai_type)

chai_type.update({"Black"})
print(chai_type)

more_chai = {"Herbal", "Earl Grey"}
chai_type.update(more_chai)

print(chai_type)

chai_type.pop()
print(chai_type)

# chai_type.remove("Herbal")
# print(chai_type)

# ? chai_type.remove("Eerl Grey") #? Generate KeyError

more_chai.clear()

print(more_chai)


for chai in chai_type:
    print(chai)


square_set = {x**2 for x in range(1, 11)}
print(square_set)

print(chai_type)

if "ginger" in chai_type:
    print("ginger tea is present in set")


chai_type_copy = chai_type.copy()
print(chai_type_copy)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 6, 7, 4}

print(s1)
print(s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print(s1 ^ s2)

print(s1.isdisjoint(s2))

x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 10}

print(x.isdisjoint(y))

print(s1.issubset(s2))

x1 = {"foo", "bar", "baz"}
print(x1.issubset({"foo", "bar", "baz", "qux", "quux"}))

x2 = {"foo", "bar", "baz", "qux", "quux"}
print(x2.issuperset(x1))
print(x1.issubset(x2))
print(x1.issuperset(x2))
tea_types=("Black","Green","Oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])
print(len(tea_types))

# ^ Immutable
# tea_types[0]="Lemon"
# print(tea_types)

more_tea = ("Herbal","Earl Grey")
all_tea= tea_types + more_tea
print(all_tea)

if "Green" in all_tea:
    print("I have a green tea")


more_tea = ("Herbal", "Earl Grey","Herbal")
print(more_tea.count("Herbal"))

(black,green,Oolang)=tea_types
print(black)
print(green)
print(Oolang)

print(type(tea_types))

# ("",(1,2,3),"")
chai_type={"Masala":"Spicy",
           "Ginger":"Zesty",
           "Green":"Mild"
           }
print(chai_type)
print(chai_type['Masala'])
print(chai_type.get("Ginger"))
print(chai_type.get("Gingery")) #? None

chai_type["Green"]="Fresh"
print(chai_type)

for chai in chai_type:
    print(f"{chai}:{chai_type[chai]}")

for key,values in chai_type.items():
    print(key,values)

if "Masala" in chai_type:
    print("I have masala chai")

print(len(chai_type))

chai_type["Earl Grey"]="Citrus"
print(chai_type)

print(chai_type.pop("Ginger"))
print(chai_type)


print(chai_type.popitem())
print(chai_type)

del chai_type["Green"]
print(chai_type)

chai_type_copy = chai_type.copy()

tea_shop={
    "chai":{
        "Masala":"Spicy",
        "Ginger":"Zesty",
    },
    "Tea":{
        "Green":"Mild",
        "Black":"Strong"
    }  
}

print(tea_shop)
print(tea_shop['chai']['Ginger'])


squared_nums={
    x:x**2 for x in range(10)
}

print(squared_nums)
squared_nums.clear()
print(squared_nums)

keys={"Masala","Ginger","Lemon"}
print(keys)
default_value="Delicious"

new_dict = dict.fromkeys(keys,default_value)
print(new_dict)

new_dict = dict.fromkeys(keys,keys)
print(new_dict)



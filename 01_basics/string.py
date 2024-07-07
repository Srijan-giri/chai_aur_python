# ^ String is immutable


print("Srijan Giri")
str = """
       Hello Everyone,
       my name is Srijan
"""
print(str)

chai = "Masala chai"
print(chai)

first_char=chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

num_list="0123456789"

print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])


chai="Masala CHai"
print(chai)
print(chai.lower())
print(chai.upper())
print(chai)  # ? String is immutable

chai="   Maslala Chai   "
print(chai)
print(chai.strip())

chai="Lemon Chai"
print(chai.replace("Lemon","Ginger"))


chai="Lemon, Ginger, Masala, Mint"

# * string to list : split()

print(chai.split())
print(chai.split(", "))

chai="Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai")) #? -1 if not found
print(chai.find("a"))
print(chai.find("a",4,9))

chai="Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai"
print(order)
print(order.format(quantity,chai_type))

order1=f"I ordered {quantity} cups of {chai_type} chai"
print(order1)


chai_variety = ["Lemon","Masala","Ginger"]
print(chai_variety)

# * list to string:join()

print("".join(chai_variety))
print(", ".join(chai_variety))


chai="Masala Chai"
print(len(chai))

for letter in chai:
    print(letter,end="")

print()

chai="He said,\"Masala chai is awasome\""
print(chai) 

print("/\\/\\/\\")

chai="Masala\nChai"
print(chai)
chai = r"Masala\nChai"
print(chai)

chai=r"c:\\user\\pwd\\"
print(chai)

chai = r"c:\user\pwd"
print(chai)

chai="Masala Chai"
print("Masala" in chai)
print("Masala Chaiii" in chai)

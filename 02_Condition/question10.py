# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter the pet")
age = int(input("Enter the age"))

if pet=="Dog":
    if age<2:
        food = "Puppy food"
if pet=="Cat":
    if age>5:
        food = "Senior cat food"


print(food)

# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

# duplicate=""

# for item in items:
#     if items.count(item)>1:
#         duplicate=item
#         break

# print(duplicate)

unique_items=set()

for item in items:
    if item in unique_items:
        print("Duplicate: ",item)
        break
    unique_items.add(item)
# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter the coffe size: ")
extra_shot = True

if extra_shot:
    coffe=order_size+" coffe with an extra shot"
else:
    coffe = order_size + " coffe"


print("Order: ",coffe)
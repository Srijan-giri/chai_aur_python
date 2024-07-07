# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    valid_input = int(input("Enter the input: "))

    if valid_input>=1 and valid_input<=10:
        print("Valid Input,Thanks !!")
        break
    else:
        print("Invalid input, try again")




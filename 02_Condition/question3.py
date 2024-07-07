# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score: "))

if score>=101:
    print("Please verify your grade again")
    exit()

if score >= 90 and score <= 100:
    grede = "A"
elif score >= 80 and score <= 89:
    grede = "B"
elif score >= 70 and score <= 79:
    grede = "C"
elif score >= 60 and score <= 69:
    grede = "D"
else:
    grede = "F"

print("Grade: ",grede)

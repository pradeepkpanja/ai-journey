#ask user input to positive or negative number

number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:   
    print("The number is zero.")


# Check if the number is even or odd

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Ask the user to enter percentage score

percentage = float(input("Enter your percentage score: "))

if percentage >= 85:
    print("Distinction")
elif percentage >= 50:
    print("Pass")
else:
    print("Fail")

#Ask the user to check age eligibility for AI roles
age = int(input("Enter you age for AI roles: "))
if age < 18:
    print("You are not eligible for AI roles.")
elif age < 60:
    print("You are eligible for AI roles.")
else:
    print("Retirement? Still want to work in AI? That's impressive!")



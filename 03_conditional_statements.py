# If statement
x = 10
if x > 5:
    print("x is greater than 5")

# If-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# Elif statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

# Nested if statement
a = 15
if a > 10:
    if a % 2 == 0:
        print("a is greater than 10 and even")
    else:
        print("a is greater than 10 but odd")
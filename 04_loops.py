#Let us learn how for loops, while loops, nested loops, break and continue statements work in Python.


# For loop example

# Loop through a range of numbers

for i in range(1, 11):
    print(f"Number: {i}")

# ask for a number N and print the numbers

N = int(input("Enter a number N: "))

for i in range(1, N + 1):
    print(f"Number: {i}")


# use a while loop to print the number 5 down to 1

countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

# AI tools

ai_tools = ["ChatGPT", "Bard", "Claude", "Gemini", "LLaMA"]

# Loop through the AI tools list and print each tool in numbers
for index in range(len(ai_tools)):
    print(f"AI Tool {index + 1}: {ai_tools[index]}")
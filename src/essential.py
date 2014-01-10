# Essentials
# Hello, world!
# Output
print("Hello, world")
# Input
i1 = input("What is your name?")
i2 = int(input("How old are you?"))
i3 = bool(int(input("Are you married")))
print("\nStatus:\nName: ", i1, "\nAge: ", i2, "\nMarried: ", i3, "\n")
# Loop
a = 0
while a < 10:
    a = a + 1
    print(a)
# Conditional statments
n = int(input("Number? "))
if n < 0:
    print("The number is negative.")
else:
    print("The number is positive.")

n = int(input("How many times? "))
for x in range(1, 10):
    print("Processing", x, "...")
    for k in range(1, 10000 * x):
        pass

# Guess number
from random import randrange
print("\n")
n = randrange(100)
correct = False
t = 1
T = 6
while (not correct) and (t <= T):
    guess = int(input("Guess? "))
    if guess > n:
        print("Too large\n")
        t = t + 1
    elif guess < n:
        print("Too small\n")
        t = t + 1
    else:
        correct = True
if correct and (t <= T):
    print("Your guess is correct!")
elif (not correct) and (t > T):
    print("Game over. The number is", n)

# Defining functions


def abs(n):
    if n < 0:
        n = -n
        return n


def hello():
    print("Hello, world!")


def area(width, height):
    return width * height

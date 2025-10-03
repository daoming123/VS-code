"""age."""
while True:
    age = input("\nPlease enter your age (or type 'quit' to stop): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("You get in for free!")
    elif age < 12:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $15.")

active = True

while active:
    age = input("\nPlease enter your age (or type 'quit' to stop): ")

    if age == 'quit':
        active = False
    age = int(age)
    if age < 3:
        print("you get in for free!")
    elif age < 18:
        print("your ticket price is $10.")
    else:
        print("your ticket price is $15.")


age = input("\nPlease enter your age (or type 'quit' to stop): ")

while age != 'quit':

    age = int(age)
    if age < 3:
        print("you get in for free!")
    elif age < 18:
        print("your ticket price is $10.")
    else:
        print("your ticket price is $15.")

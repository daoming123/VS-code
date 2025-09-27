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

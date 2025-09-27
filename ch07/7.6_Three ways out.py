"""user_input."""
user_input = input("Please enter the pizza toppings you would like to add. ")
while user_input != "quit":
    print(f"This topping has been added to pizza {user_input}\n")
    user_input = input("Please enter the pizza toppings you would like to add. ")

active = True

while active:
    user_input = input("Please enter the pizza toppings you would like to add"
    "(type 'quit' to stop): ")

    if user_input == 'quit':
        active = False
    else:
        print(f"This {user_input} topping has been added to pizza \n")

while True:
    user_input = input("Please enter the pizza toppings you would like to add"
    "(type 'quit' to stop): ")
    if user_input == 'quit':
        break
    else:
        print(f"This {user_input} topping has been added to pizza \n")

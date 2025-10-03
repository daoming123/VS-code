"""responses."""
responses = {}
polling_active = True
while polling_active:
    user_name = input("\nwhat your name? ")
    response = input("\nIf you could visit one place in the world,"
    "where would you go? ")
    responses[user_name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n --- poll Results --- ")
for user_name, response in responses.items():
    print(f"{user_name} wants to go to {response}.")

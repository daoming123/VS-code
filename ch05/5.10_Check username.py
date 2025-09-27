"""Current_users."""
current_users = ['Mary', 'Admin', 'Jaden', 'Sara', 'Luna']
new_users = ['Mary', 'Suki', 'Jami', 'Yuki', 'Lim']

current_users_upper = []
for user in current_users:
    current_users_upper.append(user.upper())
for new_user in new_users:
    if new_user.upper() in current_users_upper:
        print(f"Sorry, the {new_user}  has already been taken."
"Please choose another one.")
    else:
        print("The username {new_user} is available")

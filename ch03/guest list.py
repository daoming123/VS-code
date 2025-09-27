guest_list = ['Mary', 'Angle', 'Lida']
print(guest_list)
invitation_letter_1 = f"Can I invite you to dinner,{guest_list[0]}?"
print(invitation_letter_1)
invitation_letter_2 = f"Can I invite you to dinner,{guest_list[1]}?"
print(invitation_letter_2)
invitation_letter_3 = f"Can I invite you to dinner,{guest_list[2]}?"
print(invitation_letter_3)
guest_list[0] = 'Suki'
print(guest_list)
new_invitation_letter_1 = f"Can I invite you to dinner,{guest_list[0]}?"
print(invitation_letter_1)
new_invitation_letter_2 = f"Can I invite you to dinner,{guest_list[1]}?"
print(invitation_letter_2)
new_invitation_letter_3 = f"Can I invite you to dinner,{guest_list[2]}?"
print(invitation_letter_3)
print("Look,I found a bigger dining table.")
guest_list.insert(0, 'Star')
guest_list.insert(1, 'Sara')
guest_list.append('Yuki')
print(guest_list)
lette_1 = (f"Dear {guest_list[0]}, please come to dinner.")
lette_2 = (f"Dear {guest_list[1]}, please come to dinner.")
lette_3 = (f"Dear {guest_list[2]}, please come to dinner.")
lette_4 = (f"Dear {guest_list[3]}, please come to dinner.")
lette_5 = (f"Dear {guest_list[4]}, please come to dinner.")
lette_6 = (f"Dear {guest_list[5]}, please come to dinner.")
print(lette_1)
print(lette_2)
print(lette_3)
print(lette_4)
print(lette_5)
print(lette_6)
print(f"I am inviting {len(guest_list)} guests to my dinner party.")
print("Sorry,The newly purchased dining table could not be delivered in time,\nOnly two people can be invited to dinner")
popped_guest_list = guest_list.pop()
print (f"Sorry, I can't invite you to dinner,{popped_guest_list}.")
popped_guest_list = guest_list.pop()
print (f"Sorry, I can't invite you to dinner,{popped_guest_list}.")
popped_guest_list = guest_list.pop()
print (f"Sorry, I can't invite you to dinner,{popped_guest_list}.")
popped_guest_list = guest_list.pop()
print (f"Sorry, I can't invite you to dinner,{popped_guest_list}.")
print(f"welcome to my dinner party,{guest_list[0]}.")
print(f"welcome to my dinner party,{guest_list[1]}.")
del guest_list[1]
del guest_list[0]
print(guest_list)


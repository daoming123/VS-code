"""Nvestigation."""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python'}
people = ['jen', 'milk', 'edward', 'phil', 'sarah']
for person in people:
    if person in favorite_languages:
        print(f"hello,thank you {person}")
    else:
        print(f"Invite to take part in survey,{person}")

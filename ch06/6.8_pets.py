pet = {'kind': 'dog', 'owner_name': 'mary'}
pet_2 = {'kind': 'cat', 'owner_name': 'lynn'}
pet_3 = {'kind': 'hedgehog', 'owner_name': 'angle'}
pets = [pet, pet_2, pet_3]
for pet in pets:
    print(f"\npet kind: {pet['kind'].title()}")
    print(f"owner_name: {pet['owner_name'].title()}")

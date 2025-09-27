animals = ["dog", "cat", "elephant", "tiger", "lion", "horse", "rabbit"]
print("The first three items in the list are:")
print(animals[:3])

print("Three items from the middle of the list are:")
for animal in animals[2:5]:
    print(animal.title())

print("The last three items in the list are:")
print(animals[-3:])

"""mountains."""
mountains = ["Himalayas", "Andes", "Alps", "Rockies", "Kunlun"]
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)

instruments = ["Piano", "Guitar", "Violin", "Drums", "Flute"]

print("Here is the original list:")
print(instruments)
print("\nHere is the sorted list:")
print(sorted(instruments))
print("\nHere is the original list again:")
print(instruments)
print(sorted(instruments, reverse=True))
print(len(instruments))

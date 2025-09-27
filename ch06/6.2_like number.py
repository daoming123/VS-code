numbers = {
    'Luna': [15, 16], 'Romi': [25, 17], 'Suki': [24, 18],
           'Yuki': [99, 19], 'Mary': [67, 40]
           }
for name, nums in numbers.items():
    print(f"{name.title()} like number are : ")
    for num in nums:
        print(f"\t{num}")

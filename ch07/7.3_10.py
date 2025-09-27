"""number."""
number = input("Enter a number, and I'll tell you if it's evenMultiples of 10 or no. ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is evenMultiples of 10.")
else:
    print(f"\nThe number {number} is no evenMultiples of 10.")

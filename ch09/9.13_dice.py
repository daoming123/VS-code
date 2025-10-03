"""丢骰子."""


from random import randint


class Die:
    """创建一个骰子."""

    def __init__(self, sides=6):
        """6面骰子."""
        self.sides = sides

    def roll_die(self):
        """掷骰子."""
        return randint(1, self.sides)


die_6 = Die(6)
print("6面骰子:")
for _ in range(10):
    print(die_6.roll_die())

die_10 = Die(10)
print("\n10面骰子:")
for _ in range(10):
    print(die_10.roll_die())

die_20 = Die(20)
print("20面骰子:")
for _ in range(10):
    print(die_20.roll_die())

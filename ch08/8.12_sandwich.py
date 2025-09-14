def make_sandwich(*toppings):
    """概述要制作的三明治"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
make_sandwich('mushrooms', 'green peppers')
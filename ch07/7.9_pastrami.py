sandwich_orders = ['pastrami', 'strawberry cream sandwich',
                   'pastrami','pastrami',
                    'blueberry sandwich']
print("The pastrami at the deli is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    current_sandwich_order = sandwich_orders.pop(0)
    print(f"in production: {current_sandwich_order.title()}")
    finished_sandwiches.append(current_sandwich_order)
print("\nThe following sandwiches are ready:")
for finished_sandwiche in finished_sandwiches:
    print(f"I made your {finished_sandwiche}")
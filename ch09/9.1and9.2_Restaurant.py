class Restaurant:
    """餐馆营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印restaurant_name 和 cuisine_type"""
        print(f"The restaurant_name is {self.restaurant_name}.")
        print(f"The cuisine_type is {self.cuisine_type}")

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(f"The {self.restaurant_name} is open")

my_restaurant = Restaurant('Good luck', 'Noodle')
her_restaurant = Restaurant('Good morning', 'Rice')
his_restaurant = Restaurant('Good afternoon', 'Beef')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

her_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()


    
    
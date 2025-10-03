

class Restaurant:
    """餐馆营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印restaurant_name 和 cuisine_type"""
        print(f"The restaurant_name is {self.restaurant_name}.")
        print(f"The cuisine_type is {self.cuisine_type}")

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(f"The {self.restaurant_name} is open")

    def show_number_served(self):
        """打印有多少人在这家餐馆就餐过"""
        print(f"{self.number_served} people have dined at this restaurant.")

    def set_number_served(self,number):
        """设置就餐人数为指定的值"""
        self.number_served = number
    
    def increment_number_served(self, number_of_diners):
        """用来让就餐人数递增"""
        self.number_served += number_of_diners
        print(f"After serving {number_of_diners} more diners, "
              f"the total is now {self.number_served}.")

restaurant = Restaurant('Hello', 'POrk')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.show_number_served()

restaurant.set_number_served(40)
restaurant.show_number_served()

restaurant.increment_number_served(50)
restaurant.show_number_served()
class Car:
 """一次模拟汽车的简单尝试"""
 def __init__(self, make, model, year):
    """初始化描述汽车的属性"""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
 def get_descriptive_name(self):
    """返回格式规范的描述性名称"""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
 def read_odometer(self):
    """打印一个句子，指出汽车的行驶里程"""
    print(f"This car has {self.odometer_reading} miles on it.")
 def update_odometer(self, mileage):
    """将里程表读数设置为给定的值"""
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
         print("You can't roll back an odometer!")

 def increment_odometer(self, miles):
    """让里程表读数增加给定的量"""
    self.odometer_reading += miles
class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
             range = 150
        elif self.battery_size == 65:
             range = 225
        print(f"This car can go about {range} miles on a full charge.")


    def upgrade_battery(self,battery_size=65):
       """检查电池容量，如果不是 65，就升级为 65"""
       if self.battery_size < 65:
           self.battery_size = 65
           print("Battery upgraded to 65-kWh.")
       else:
           print("The battery is already at 65-kWh.")
           


    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
             range = 150
        elif self.battery_size == 65:
             range = 225
        print(f"This car can go about {range} miles on a full charge.")

       
       
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
    

my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range() 

my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
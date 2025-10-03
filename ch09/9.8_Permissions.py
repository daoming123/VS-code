<<<<<<< HEAD
class User:
    """用户实例"""
    def __init__(self, first_name , last_name, age, gender):
        """初始化属性 first_name 和last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Privileges():
    """创建一个权限"""

    def __init__(self):
        self.privileges = ["can add post", "can deletepost", "can ban user"]

    def show_privileges(self):
        print("Administrator permissions include:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    """管理员"""
    def __init__(self, first_name , last_name, age, gender):
        super().__init__ (first_name, last_name, age, gender)
        self.privileges = Privileges()
    
admin_1 = Admin('Dao', 'Ming', 20, 'Female')
admin_1.privileges.show_privileges()

=======
class User:
    """用户实例"""
    def __init__(self, first_name , last_name, age, gender):
        """初始化属性 first_name 和last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Privileges():
    """创建一个权限"""

    def __init__(self):
        self.privileges = ["can add post", "can deletepost", "can ban user"]

    def show_privileges(self):
        print("Administrator permissions include:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    """管理员"""
    def __init__(self, first_name , last_name, age, gender):
        super().__init__ (first_name, last_name, age, gender)
        self.privileges = Privileges()
    
admin_1 = Admin('Dao', 'Ming', 20, 'Female')
admin_1.privileges.show_privileges()

>>>>>>> ddb9f76865614855e9dbead36ef2c8d652b156f5
    
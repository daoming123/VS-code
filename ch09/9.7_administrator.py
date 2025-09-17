class User:
    """用户实例"""
    def __init__(self, first_name , last_name, age, gender):
        """初始化属性 first_name 和last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Admin(User):
    """管理员"""
    def __init__(self, first_name , last_name, age, gender):
        """初始化父类属性"""
        super().__init__ (first_name, last_name, age, gender)
        self.privileges = ["can add post", "can deletepost", "can ban user"]

    def show_privileges(self):
        print(f"Administrator permissions include:{self.privileges}")

Admin_1 = Admin('Dao', 'Ming', 20, 'Female')
Admin_1.show_privileges()




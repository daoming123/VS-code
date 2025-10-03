"""User."""


class User:
    """用户实例."""

    def __init__(self, first_name, last_name, age, gender):
        """初始化属性 first_name 和last_name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """描述用户."""
        username = "f{self.first_name} {self.last_name}"
        print(f"user.infor: {username, self.age, self.gender}")

    def greet_user(self):
        """问候用户."""
        username = "f{self.first_name} {self.last_name}"
        print(f"Hello, {username}")


user_1 = User('Dao', 'Ming', 20, 'Female')
user_2 = User('Xiao', 'Hong', 25, 'Female')
user_3 = User('Xiao', 'Ming', 30, 'Male')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

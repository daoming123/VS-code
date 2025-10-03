"""用户实例."""


class User:
    """用户实例."""

    def __init__(self, first_name, last_name, age, gender):
        """初始化属性 first_name 和last_name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要."""
        username = f"{self.first_name} {self.last_name}"
        print(f"User infor: {username}, Age: {self.age}, Gender: {self.gender}")

    def greet_user(self):
        """个性化问候."""
        username = f"{self.first_name} {self.last_name}"
        print(f"Hello, {username}")

    def increment_login_attempts(self):
        """登录次数加 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置登录次数为 0."""
        self.login_attempts = 0


user_1 = User('Dao', 'Ming', 20, 'Female')
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"Login attempts after reset: {user_1.login_attempts}")

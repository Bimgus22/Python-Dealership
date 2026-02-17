class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")


user1 = User("Jake", "Bush", 21, "jake@example.com", "South Carolina")
user2 = User("Maria", "Lopez", 22, "maria@example.com", "Texas")
user3 = User("Ethan", "Clark", 20, "ethan@example.com", "California")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
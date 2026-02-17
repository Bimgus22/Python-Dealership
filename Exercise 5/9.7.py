class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin1 = Admin("Jake", "Bush", "admin@example.com")
admin1.show_privileges()

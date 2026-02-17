class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} ({self.email})")


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()
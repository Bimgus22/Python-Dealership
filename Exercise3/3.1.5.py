valid_flavours = [
    "ubuntu", "kubuntu", "xubuntu", "lubuntu", "ubuntu mate",
    "ubuntu studio", "ubuntu budgie", "ubuntu kylin", "ubuntu minimal"
]

user_flavours = {}

print("Welcome to the Ubuntu Flavour Poll!")
print("Valid flavours are:", ", ".join(valid_flavours))
print("Type 'quit' as your username to stop the poll.\n")

while True:
    username = input("Enter your username (or type 'quit' to exit): ").strip()

    if username.lower() == "quit":
        print("\nThank you for participating in the poll!")
        break

    flavour = input(f"Hi {username}, what is your favorite Ubuntu flavour? ").strip().lower()
    if flavour in valid_flavours:
        user_flavours[username] = flavour
        print(f"Thanks {username}, your favourite flavour '{flavour.title()}' has been recorded!\n")
    else:
        print(
            f"'{flavour}' is not a legitimate Ubuntu flavour. "
            f"Please choose from: {', '.join(valid_flavours)}\n"
        )
print("Poll results:")
for user, flavour in user_flavours.items():
    print(f"{user}: {flavour.title()}")

print("Enter names for the guest book.")
print("Type 'q' to quit.\n")

with open("guest_book.txt", "a") as file_object:
    while True:
        name = input("Enter your name: ")

        if name.lower() == 'q':
            break

        print(f"Hello, {name}! You have been added to the guest book.")
        file_object.write(name + "\n")
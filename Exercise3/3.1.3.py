while True:
    user_input = input("Enter an integer (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    try:
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is even.\n")
        else:
            print(f"{number} is odd.\n")
    except ValueError:
        print("That's not a valid integer. Please try again.\n")
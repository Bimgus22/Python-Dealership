active = True
total = 0

while active:
    user_input = input("Enter a number to add to the total (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    try:
        number = float(user_input)
        total += number
        print(f"Current total is: {total}\n")
    except ValueError:
        print("That's not a valid number. Please try again.\n")
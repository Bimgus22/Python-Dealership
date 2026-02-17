print("Enter two numbers to add them together.")
print("Type 'q' at any time to quit.\n")

while True:
    first = input("First number: ")
    if first.lower() == 'q':
        break

    second = input("Second number: ")
    if second.lower() == 'q':
        break

    try:
        num1 = int(first)
        num2 = int(second)
        result = num1 + num2
    except (ValueError, TypeError):
        print("Sorry, please enter valid numbers only.\n")
    else:
        print(f"The sum is {result}.\n")
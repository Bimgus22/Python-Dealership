print("Addition Calculator")
print("Enter 'q' at any time to quit.\n")

while True:
    first = input("First number: ")
    if first.lower() == 'q':
        break

    second = input("Second number: ")
    if second.lower() == 'q':
        break

    try:
        num1 = float(first)
        num2 = float(second)
    except ValueError:
        print("Please enter numeric values only.\n")
    else:
        print(f"Result: {num1 + num2}\n")

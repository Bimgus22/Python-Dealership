print("Programming Poll")
print("Type 'q' to quit.\n")

with open("programming_poll.txt", "a") as file_object:
    while True:
        reason = input("Why do you like programming? ")

        if reason.lower() == 'q':
            break

        file_object.write(reason + "\n")

print("Thanks for participating in the poll!")
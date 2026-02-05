money = float(input("How much money do you have to spend on a processor? $"))

if money >= 500:
    print("You can afford an Intel i9 processor.")
elif money >= 350:
    print("You can afford an Intel i7 processor.")
elif money >= 250:
    print("You can afford an Intel i5 processor.")
elif money >= 120:
    print("You can afford an Intel i3 processor.")
else:
    print("You do not have enough money to buy a new processor.")

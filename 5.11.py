numbers = list(range(1, 10))  # 1 through 9
for num in numbers:
    if num == 1:
        ending = "st"
    elif num == 2:
        ending = "nd"
    elif num == 3:
        ending = "rd"
    else:
        ending = "th"

    print(f"{num}{ending}")
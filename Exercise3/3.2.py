person = {
    "f_name": "Theodore",
    "l_name": "Roosevelt",
    "age": 42,
    "hometown": "New York",
    "current_city": "New York",
    "username": "bull_moose"
}

print(
    f"This person's first name is {person['f_name']}, "
    f"last name is {person['l_name']}, "
    f"and their username is {person['username']}."
)

print(
    f"For security reasons, we might ask them for their hometown, "
    f"which is {person['hometown']}."
)

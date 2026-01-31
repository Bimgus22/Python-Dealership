current_users = ['alice', 'bob', 'charlie', 'dave', 'emma', 'admin']
new_users = ['Frank', 'BOB', 'Grace', 'helen', 'Admin', 'ivy']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available!")
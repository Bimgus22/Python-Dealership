usernames = ['admin', 'jaden', 'sarah', 'mike', 'emma', 'liam']
for username in usernames:
    if username.lower() == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
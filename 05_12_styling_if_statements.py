current_users = ['Bobby', 'Kyle', 'Admin', 'Hailey', 'Jaden']

new_users = ['John', 'Hunter', 'Barry', 'Axel', 'Teddy']

lowercase_current_users = [user.lower() for user in current_users]


for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"Sorry, the username '{new_user}' has already been taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_username(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    movie = input("What's your favorite movie? ")
    animal = input("What's your favorite animal? ")

    user_dict = {'username': username,'movie': movie,'animal': animal,}

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict
def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info.json')
    user_dict = get_stored_username(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been enjoying the movie {user_dict['movie']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_username(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()

users = {'GEF': {'first': 'Greg','last': 'Fulltur','location': 'Ohio','age': 30,'favorite_books': ['House of Earth and Bloos', 'Favorite Person: Tom Hardy']},'K00P': {'first': 'Keith','last': 'Pilester','location': 'Africa','age': 75,'favorite_books': ['Beowulf Unknown', 'Anglo-Saxon ']},}

for username, user_info in users.items():
    print(f"\nUsername: {username}")  
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location']  
    age = user_info['age']  
    favorite_books = user_info['favorite_books'] 

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tAge: {age}")
    print("\tFavorite Books:")
    
    for book in favorite_books:
        print(f"\t{book}")

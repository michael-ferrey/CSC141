favorite_places = {'Herny': ['Reading', 'Bethlehem', 'Mexico'],'Jackson': ['United Kingdom', 'Denmark'],'Perry': ['Chile', 'Massachusettes', 'Mississippi']}

for name, places in favorite_places.items():

    print(name + "'s favorite places are:\n")

    for place in places:
        print(place)
    print()

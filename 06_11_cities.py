cities = {'Bethlehem': {'country': 'USA','population': 78300,'fact': 'It is known as Christmas City.' },'Namur': {'country': 'Belgium','population': 112065,'fact': 'The city between Meuse River and Sambre River.'},'Cape Town': {'country': 'Africa','population': 4773000,'fact': 'It is known for its ranges of stunning nautral wonders.'}}

for city, info in cities.items():  
    print("City:", city)  
    print("Country:", info['country'])  
    print("Population:", info['population'])  
    print("Fact:", info['fact'])  
    print()

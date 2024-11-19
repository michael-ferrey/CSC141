fav_numbers = {'James': [4, 21, 79],'Hurtbert': [13, 33],'Logan': [84, 105],'Greg': [60, 2, 50],'Walley': [34, 99]}

for name in fav_numbers: 
    print(name + "'s favorite numbers are:")  
    for number in fav_numbers[name]:  
        print(str(number)) 
    print()

dream_Vacations = []

while True:
    vacation = input("If you could go and visit one place in the wolrd, where would you go? (type 'quit' to finish): ")
    
    if vacation.lower() == 'quit':
        break
    
    dream_Vacations.append(vacation)

print("\nDream Vacation Destinations:")
for destination in dream_Vacations:
    print(destination)

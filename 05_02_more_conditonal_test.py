car = 'subaru'
foods = ['bacon', 'pasta', 'salad']
age = 18


print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


print("\nIs car != 'mercedes'? I predict True.")
print(car != 'mercedes')


print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')


print("\nIs car.lower() == 'SUBARU'? I predict False.")
print(car.lower() == 'SUBARU')


print("\nIs age == 18? I predict True.")
print(age == 18)


print("\nIs age > 49? I predict False.")
print(age > 49) 


print("\nIs age < 32? I predict True.")
print(age < 32)

print("\nIs age >= 19? I predict True.")
print(age >= 19)

print("\nIs age <= 14? I predict False.")
print(age <= 14)

print("\nIs car == 'subaru' and age < 40? I predict True.")
print(car == 'subaru' and age < 40)

print("\nIs car == 'buick' and age < 10? I predict False.")
print(car == 'buick' and age < 10)

print("\nIs car == 'subaru' or age > 20? I predict True.")
print(car == 'subaru' or age > 20)

print("\nIs car == 'honda' or age < 15? I predict False.")
print(car == 'honda' or age < 15)


print("\nIs 'pasta' in foods? I predict True.")
print('pasta' in foods)

print("\nIs 'tacos' in foods? I predict False.")
print('tacos' in foods)

print("\nIs 'bacon' not in foods? I predict False.")
print('bacon' not in foods)

print("\nIs 'rice' not in foods? I predict True.")
print('rice' not in foods)

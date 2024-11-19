toppings = []
active = True 

while active:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break  

    toppings.append(topping)
    print("I'll add " + topping + " to your pizza.")

print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(topping)

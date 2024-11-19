while True:
    age = input("Please enter your age (or type 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        price = "free"
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print("The ticket price is $" + str(price) + ".")

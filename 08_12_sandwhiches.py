def make_sandwich(*items):
    print("The sandwich you ordered has:")
    for item in items:
        print(item)
    print()

make_sandwich("lettuce", "bacon", "cheese")
make_sandwich("ham", "cheese")
make_sandwich("turkey", "cheese", "lettuce", "totmotes")

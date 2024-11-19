sandwich_Orders = ['ham', 'cheese', 'italian', 'meat', 'bologna']

finished_Sandwiches = []

for sandwich in sandwich_Orders:
    print("I have made your " + sandwich + " sandwich.")

    finished_Sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for finished_Sandwich in finished_Sandwiches:
    print(finished_Sandwich)

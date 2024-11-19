sandwich_Orders = ['ham', 'cheese', 'pastrami', 'italian', 'pastrami', 'meat', 'pastrami', 'bologna']

finished_Sandwiches = []

print("The deli has run out of pastrami sandwiches!")

while 'pastrami' in sandwich_Orders:
    sandwich_Orders.remove('pastrami')

for sandwich in sandwich_Orders:
    print("I made your " + sandwich + " sandwich.")

    finished_Sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for finished_Sandwich in finished_Sandwiches:
    print(finished_Sandwich)

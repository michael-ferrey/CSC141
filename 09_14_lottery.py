import random

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_combination = random.sample(items, 4)

print(f"Congratulations! Any ticket matching these four items wins a prize: {winning_combination}")

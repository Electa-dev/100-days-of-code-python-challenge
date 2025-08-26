import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
roulette_loser = random.choice(friends)
print(roulette_loser)
print(f"{roulette_loser} you are to pay the bills.")

# WE could also do this
random_name = random.randint(0, 4)
print(friends[random_name])

import random

rolls = []
num_6 = 0
num_1 = 0
num_two_6s_in_a_row = 0

for _ in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        num_6 += 1
        if len(rolls) >= 2 and rolls[-2] == 6:
            num_two_6s_in_a_row += 1
    elif roll == 1:
        num_1 += 1

print(f"Number of times rolled a 6: {num_6}")
print(f"Number of times rolled a 1: {num_1}")
print(f"Number of times rolled two 6s in a row: {num_two_6s_in_a_row}")

import random

# main routine goes here

tokens = ["unicorn", "horse","horse","horse",
          "zebra","zebra","zebra",
          "donkey","donkey","donkey",]
starting_balance = 100

balance = starting_balance
# testing loop to generate 20 tokens
for item in range(0, 20):
    chosen_num = random.randint(1,100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"

    elif 6 <= chosen_num <36:
        chosen = "donkey"

print()
print("starting Balance: ${:.2f}" .format(starting_balance))
print("Final Balance: ${:.2f}".format(balance))


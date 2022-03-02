import random

# main routine goes here

tokens = ["unicorn", "horse","horse","horse",
          "zebra","zebra","zebra",
          "donkey","donkey","donkey",]
starting_balance = 100

balance = starting_balance
# testing loop to generate 20 tokens
for item in range(0, 20):
    number = random.randint(1, 4)
    print(number, end="\t")

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("starting Balance: ${:.2f}" .format(starting_balance))
print("Final Balance: ${:.2f}".format(balance))


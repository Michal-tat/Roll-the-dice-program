import random
def roll():
    x = random.randint(1, 6)
    print("the number is:")
    print (x)
    print("would you like to roll the dice again?")
    y = input()
    if y == "yes":
        repeat(x)
    if y == "no":
        return

def repeat(x):
    x = roll()

roll()
import random
import os
def cls(): os.system('cls')

r = random.randint(1, 5)

def guess_random(r):
    while True:
        n = int(input("Guess: "))

        cls()

        if n == r: break
        else:
            if n > r:
                print("Lower")
            else:
                print("Higher")

guess_random(r)
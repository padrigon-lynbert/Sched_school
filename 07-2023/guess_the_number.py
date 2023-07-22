import random
import os
def cls(): os.system('cls')

r = random.randint(1, 1000)

def guess_random(random_number): 
    while True:
        n = int(input("Guess: "))

        cls()

        if n == random_number: 
            print(f"Congratulations on guessing the random number \"{random_number}!\"")
            break
        else:
            if n > random_number:
                print("Lower")
            else:
                print("Higher")

guess_random(r)

        
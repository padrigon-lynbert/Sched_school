import random
import os

def cls(): os.system('cls')

def play():
    user = input("r for rock, p for paper, s for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'
    
    if is_win(user, computer):
        return 'You Won'
    
    return 'You Lost'

def is_win(player, computer):
    #r>s p>r s>p
    # return true if player wins

    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True
    
while True:

    [print(play()) for i in range(5)]
    r = input("continue playing? <y> or <n> : ")
    if r == 'n': break
    else: cls()

    

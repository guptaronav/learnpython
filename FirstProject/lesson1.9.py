import random

moves = ['r','p','s']
player_wins = ['pr','sp','rs']
name = input("What's your name? ").capitalize()

n_playerwins = 0
n_computerwins = 0
for i in range(3):
    player_move = input(name + "'s move: ")
    computer_move = random.choice(moves)

    print(name + "'s Move: ", player_move)
    print("Computer's Move: ", computer_move)

    if player_move == computer_move:
        print("TIE")
    elif player_move + computer_move in player_wins:
        print("YOU WON!")
        n_playerwins = n_playerwins + 1
    else:
        print("YOU LOST!")
        n_computerwins = n_computerwins + 1

print(name + "'s score is ", n_playerwins)
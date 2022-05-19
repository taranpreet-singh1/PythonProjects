#Thanks to freecodecamp.org for this project idea and assistance

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors \n") #input from user 
    computer = random.choice(['r','p','s']) #computer's choice
    
    if user == computer: #Both chose same thing
         print("It\'s a Tie")

    if is_win(user, computer): #User won
        print("You won!")

    if is_win(computer,user): #Computer wins
        print("You lost")

def is_win(player,opponent):
    #return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play()
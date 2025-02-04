import random
"""
Name: Aiden P.
File: rps_minus_one.py
Description: Implements Rock Paper Scissors Minus One from Squid Game
"""

"""
Pseudo Code
- Have computer pick RPS twice randomly
- Set both player's score to 0
- Store values in comp_hand
- Ask Users for their hands
- Store values in player_hand
- Ask user which hand to keep
- Remove a variable
- Computer randomly chooses which hand to keep
- Evaluate who wins
- Update score
- Ask user if they want to play again
- If they quit, print scores and end game
- otherwise play again
"""

def comp_hand():
    hand1 = (random.randint(1,3))
    hand2 = (random.randint(1,3))
    if hand1 == 1:
        compint = "Rock"
    elif hand1 == 2:
        compint = "Paper"
    elif hand1 == 3:
        compint = "Scissors"
    if hand2 == 1:
        compint2 = "Rock"
    elif hand2 == 2:
        compint2 = "Paper"
    elif hand2 == 3:
        compint2 = "Scissors"
    return(compint,compint2)
def player_hand():
    handinput = input("What are you gonna throw first?: ")
    if handinput == "rock":
        handint = 1
    elif handinput == "paper":
        handint = 2
    elif handinput == "scissors":
        handint = 3
    handinput2 = input("What are you gonna throw next?: ")
    if handinput2 == "rock":
        handint2 = 1
    elif handinput2 == "paper":
        handint2 = 2
    elif handinput2 == "scissors":
        handint2 = 3
    return(handint,handint2)

def main():
    player_hand()
    print(comp_hand())
    print(player_hand)


main()










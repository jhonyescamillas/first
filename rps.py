import random
import sys


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def main():
# game logic
# clears screen before start of a new game
# asks the player the target score to reach
    print("\n" * 100)
    print("Welcome to Rock, Paper, Scissors.")
    rounds = int(input("Race to what score? "))
    counter = 1
    player_score = 0
    computer_score = 0
# keep looping until either player or computer reaches target score 
    while True:
        print(f"\nROUND {counter}")
# player inputs choice between rock (0), paper (1), or scissors (2)
        player_choice = get_choice()
# generate random computer choice
        computer_choice = random.randint(0, 2)
# show player and computer choice and display the ascii art
        display_choice(player_choice, computer_choice)
# decide winner based on choices
        winner = get_winner(player_choice, computer_choice)
# update the score
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"Your score: {player_score}\nComputer score: {computer_score}")
        print(f"This is a race to {rounds}.")
# check whether player or computer has reached the target score
# end the loop
        if player_score == rounds:
            print("\nYOU FINISHED FIRST! CONGRATULATIONS!")
            break
        elif computer_score == rounds:
            print("\nCOMPUTER FINISHED FIRST! YOU LOST!")
            break
        counter += 1
# ask whether player wants to play again
    if replay():
        main()
# exit the game
    else:
        sys.exit("\nThank you for playing Rock, Paper, Scissors!\n")


def get_choice():
    """gets player choice. Will only accept 0, 1 or 2 as input

    Returns
    -------
    integer
        a number that is used to decide the winner
    
    """

    choice = ""
    while choice not in (0, 1, 2):
        choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
    return choice
    

def display_choice(player_choice, computer_choice):
    """prints ascii art as interpretation of rock, paper, scissors

    Parameters
    ----------
    player_choice : int
        a number that is used to determine the index in the list
        0 for rock, 1 for paper and 2 for scissors 
    
    Returns
    -------
    int
        numbers that will be used to decide the winner
    """

    game_img = [rock, paper, scissors]
    print("\n" * 100)
    print(f"\nYou: \n{game_img[player_choice]}")
    print(f"\nComputer: \n{game_img[computer_choice]}")
    return player_choice, computer_choice


def get_winner(player, computer):
    """determines and prints the winner for each round
    rock beats scissors, scissors beat paper, paper beats rock

    Returns
    -------
    str
        a string that is used to update the scores and decide the overall winner
    
    """

    player = int(player)
    if player == 2 and computer == 0:
        print("\nComputer wins the round!")
        return "computer"  
    elif player == 0 and computer == 2:
        print("\nYou win the round!")
        return "player"
    elif player > computer:
        print("\nYou win the round!")
        return "player"
    elif player == computer:
        print("\nDraw!")
    else:
        print("\nComputer wins the round!")
        return "computer"


def replay():
    """asks the user if they want to keep playing
    Will only accept "y" or "n"
    
    Returns
    -------
    boolean
    """

    choice = ""
    while choice not in ("y", "n"):
        choice = input("\nPlay again? (y or n) ").lower()
    return True if choice == "y" else False
    

if __name__ == "__main__":
    main()

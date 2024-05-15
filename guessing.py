"""
A simple guessing game. Player can choose easy or hard difficulties, as well as the
level. The level is the upper limit of the number to be guessed.

The player wins if they can guess the number before their lives run out.
"""

from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def main():
    # clear the screen after each game
    print("\n" * 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("Hard = 5 attempts\nEasy = 10 attempts")
    difficulty = ""
    # only accept 'easy' or 'hard' as input
    while difficulty not in ("easy", "hard"):
        difficulty = input("Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    # loop until user inputs whole non-negative numbers
    while True:
        try:
            level = int(input("Level: "))
            if level < 2:
                print("Level cannot be lower than 2!")
            else:
                # generate a random number between 1 and the chosen level
                n = randint(2, level)
                break
        except ValueError:
            print("Numbers only!")
    print(f"I'm thinking of a number between 1 and {level}")
    # loop until user inputs whole non-negative numbers
    while True:
        try:
            # loop until lives run out or player guesses the number
            while lives > 0:
                guess = int(input("Guess: "))
                if guess < 1 or guess > level:
                    print("Oops!")
                elif guess < n:
                    lives -= 1
                    print(f"Too low!\nAttempts left: {lives}")
                elif guess > n:
                    lives -= 1
                    print(f"Too high!\nAttempts left: {lives}")
                else:
                    print(f"Just right! You got it.")
                    break
            if lives == 0:
                print(f"No more attempts left. Too bad!\nThe number is {n}")
            break
        except ValueError:
            print("Numbers only!")

    if replay():
        main()
    else:
        print("Goodbye!")


def replay():
    """ask the user if they want to play again"""
    choice = ""
    while choice not in ("yes", "no"):
        choice = input("\nType 'yes' to play again or 'no' to exit: ").lower()
    return True if choice == "yes" else False


if __name__ == "__main__":
    main()

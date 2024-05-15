from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


def main():
    print("\n" * 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = ""
    while difficulty not in ("easy", "hard"):
        difficulty = input("Hard = 5 attempts\nEasy = 10 attempts\nType 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    while True:
        try:
            level = int(input("Level: "))
            if level < 2:
                print("Level cannot be lower than 2!")
            else:
                n = randint(2, level)
                print(f"I'm thinking of a number between 1 and {level}")
                while lives > 0:
                    guess = int(input("Guess: "))
                    if guess < 2 or guess >= level:
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
        except (ValueError):
            pass

    if replay():
        main()
    else:
        print("Goodbye!")


def replay():
    choice = ""
    while choice not in ("yes", "no"):
        choice = input("\nPlay again? 'yes' or 'no': ").lower()
    return True if choice == "yes" else False


if __name__ == "__main__":
    main()

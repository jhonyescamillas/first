import random
import os

from art import vs, logo
from game_data import data


def main():
    print(logo)
    score = 0
    # assign random accounts to a and b
    account_a = random.choice(data)
    account_b = random.choice(data)
    # indicator to keep the while loop going
    game_on = True
    # keep looping until player answers incorrectly
    while game_on:
        account_a = account_b
        account_b = random.choice(data)
        # accounts cannot be the same
        # get another random account if a and b are the same
        if account_a == account_b:
            account_b = random.choice(data)
        print(f"\nA: {account_a['name']}, {account_a['description']} from {account_a['country']}")
        print(vs)
        print(f"B: {account_b['name']}, {account_b['description']} from {account_b['country']}")
        answer = input("\nWho has more followers? 'A' or 'B': ").lower()
        is_right = check_answer(answer, account_a, account_b)
        clear()
        print(logo)
        if is_right:
            score += 1
            print(f"That's right! Current score: {score}")
        else:
            print(f"Wrong answer. Final score: {score}")
            # exit the loop
            game_on = False
    if replay():
        main()
    else:
        print("\nThank you for playing!\n")

def check_answer(ans, a, b):
    """
    Compare the follower_count of a and b against each other
    and return True if the answer matches the higher count
    """
    if a["follower_count"] > b["follower_count"]:
        return ans == "a"
    else:
        return ans == "b"


def clear():
    """clear the output screen"""
    os.system("cls")


def replay():
    """ask player if they want to go again"""
    choice = ""
    while choice not in ("y", "n"):
        choice = input("\nType 'y' to play again or 'n' to exit game: ").lower()
    return True if choice == "y" else False


if __name__ == "__main__":
    main()

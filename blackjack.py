import random
import sys

# global variables
suits = ("Diamonds", "Hearts", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    """
    A class representing a Card

    Attributes
    ----------
    __str__ 
        a formatted string that prints out the Card's rank and suit
    suit : str
        the suit of a card
    rank : str
        the rank of a card
    value : int
        the value of a card in respect to its rank
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    A class representing a Deck of 52 cards

    Attributes
    ----------
    all_cards : list
        a list that contains 52 cards

    Methods
    -------
    shuffle_deck
        shuffle the deck
    remove_card
        remove one card from deck
    """

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop()


class Player:
    """
    A class representing a Player

    Attributes
    ----------
    __str__
        a formatted string that prints out player's name and number of chips
    name : str
        the player's name
    chips : int
        the player's number of chips which cannot be zero (0)
    bet : int
        the player's bet, taken against the number of chips. 
        cannot be zero, negative or more than the number of chips

    Methods
    -------
    take_loss(amount)
        deducts amount from the player's number of chips
    take_win(amount)
        adds amount to the player's number of chips
    """

    def __init__(self, name):
        self.name = name
        self.chips = 0
        self.bet = 0

    def __str__(self):
        return f"Player {self.name} has {self.chips} chips"

    def take_loss(self, amount):
        self.chips -= amount

    def take_win(self, amount):
        self.chips += amount


class Hand:
    """
    A class representing a Hand

    Attributes
    ----------
    cards : list
        a list to represent the cards in a Hand
    value : int
        a number that represents the value of a Hand
    ace : int
        a number that represents the number of "Ace" in a Hand

    Methods
    -------
    deal_card(new_card)
        adds new_card to the Hand which is taken from the Deck
    ace_adjust
        Ace can have a value of 1 or 11
        Adjust the value of Ace if the Hand's value exceeds 21 
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def deal_card(self, new_card):
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        # check if hand has an Ace
        if new_card.rank == "Ace":
            self.ace += 1

    # if hand goes over 21 and has an ace
    # value of ace will be adjusted to 1
    def ace_adjust(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


# take in player's bet
# flag if bet is more than player's chips
# only accept number input
def take_bet(player):
    while True:
        try:
            player.bet = int(input("Enter your bet: "))
            if player.bet > player.chips:
                print("You don't have enough chips!", player.chips)
            else:
                break
        except ValueError:
            print("Numbers only!")


# hide one of dealer's card and show all player's cards
def show_some(dealer, player):
    print("\nDealer:")
    print(f"???")
    print(f"{dealer.cards[1]}")
    print(f"\nPlayer Score: {player.value}")
    print(*player.cards, sep="\n")


# show all cards
def show_all_hands(dealer, player):
    print(f"\nDealer Score: {dealer.value}")
    print(*dealer.cards, sep="\n")
    print(f"\nPlayer Score: {player.value}")
    print(*player.cards, sep="\n")


# add card to hand
def hit(deck, hand):
    hand.deal_card(deck.remove_card())
    hand.ace_adjust()


# ask player whether to hit or stand
def hit_or_stand():
    choice = ""
    while choice not in ("h", "s"):
        try:
            choice = input("\nHit (h) or Stand (s)? ").lower()
        except ValueError:
            pass
    return True if choice == "h" else False


# if player's hand goes over 21, announce player loss
# display number of chips
def player_bust(player, chips):
    print(f"\nPlayer Busted! {player.name} lost!")
    player.take_loss(chips)
    print(player)


# if dealer's hand goes over 21, announce player win
# display number of chips
def dealer_bust(player, chips):
    print(f"\nDealer Busted! {player.name} won!")
    player.take_win(chips)
    print(player)


# ask player if they want to continue playing
# exit game if player's chips are less than 0 but they chose to play again
def replay(chips):
    choice = ""
    while choice not in ("y", "n"):
        try:
            choice = input("\nPlay again? ").lower()
        except ValueError:
            pass
    if chips <= 0:
        sys.exit(f"You have {chips} chips!")
    return True if choice == "y" and chips > 0 else False


def main():
    print("Welcome to Blackjack!")
    print("Get as close to 21 as you can without going over (bust).")
    print("Dealer hits until he reaches 17. Aces count as 1 or 11.")
    player = Player(input("\nEnter player name: "))
    #only accpet whole numbers as input
    while True:
        try:
            player.chips = int(input("Enter starting chips: "))
            break
        except ValueError:
            print("Numbers only!")
    # keep looping until player decides not to play again
    game_on = True
    while game_on:
        # create a deck of cards and shuffle it
        new_deck = Deck()
        new_deck.shuffle_deck()
        # assign player and dealer hands
        player_hand = Hand()
        dealer_hand = Hand()
        # add two cards to player and dealer hands
        for _ in range(2):
            player_hand.deal_card(new_deck.remove_card())
            dealer_hand.deal_card(new_deck.remove_card())
        # ask player how much to bet
        take_bet(player)
        # keep looping until player chooses to stand
        while True:
            show_some(dealer_hand, player_hand)
            if dealer_hand.value < 17:
                hit(new_deck, dealer_hand)
            if hit_or_stand():
                hit(new_deck, player_hand)
            else:
                # reveal both dealer and player hands
                show_all_hands(dealer_hand, player_hand)
                # check winner and adjust player chips
                if player_hand.value > 21:
                    player_bust(player, player.bet)
                    break
                elif dealer_hand.value > 21:
                    dealer_bust(player, player.bet)
                    break
                if dealer_hand.value < player_hand.value:
                    player.take_win(player.bet)
                    print(f"\nPlayer {player.name} wins!")
                    print(player)
                elif dealer_hand.value == player_hand.value:
                    print("\nPUSH!")
                else:
                    player.take_loss(player.bet)
                    print(f"\nPlayer {player.name} lost!")
                    print(player)
                break

        if replay(player.chips):
            continue
        else:
            game_on = False


if __name__ == "__main__":
    main()

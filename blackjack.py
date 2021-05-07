# global variables and imports
import random

# main classes


deck_of_cards = {
    "2 of diamonds": 2, "3 of diamonds": 3, "4 of diamonds": 4,
    "5 of diamonds": 5, "6 of diamonds": 6, "7 of diamonds": 7,
    "8 of diamonds": 8, "9 of diamonds": 9, "10 of diamonds": 10,
    "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds":10,
    "Ace of diamonds": 11,
    "2 of hearts": 2, "3 of hearts": 3, "4 of hearts": 4,
    "5 of hearts": 5, "6 of hearts": 6, "7 of hearts": 7,
    "8 of hearts": 8, "9 of hearts": 9, "10 of hearts": 10,
    "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts":10,
    "Ace of hearts": 11,
    "2 of spades": 2, "3 of spades": 3, "4 of spades": 4,
    "5 of spades": 5, "6 of spades": 6, "7 of spades": 7,
    "8 of spades": 8, "9 of spades": 9, "10 of spades": 10,
    "Jack of spades": 10, "Queen of spades": 10, "King of spades":10,
    "Ace of spades": 11,
    "2 of clubs": 2, "3 of clubs": 3, "4 of clubs": 4,
    "5 of clubs": 5, "6 of clubs": 6, "7 of clubs": 7,
    "8 of clubs": 8, "9 of clubs": 9, "10 of clubs": 10,
    "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs":10,
    "Ace of clubs": 11
    }


intro = """ 
\t\t\t Welcome to Blackjack! \n\n
You will play against the dealer with the amount you specify in the beginning.
Your maximum bet will be 10 percent of your starting value,
the minimum bet will be 1 percent. Each round you will be dealt 2 cards and 
be told one of the two cards of the dealer. There are 3 actions availble every round:\n
\t - Hit: You will receive another card.\n
\t - Stand: You will receive no more cards and the dealer will draw until he has 17 or more points in hand. \n
\t - Double down: You receive exactly one more card, double your bet and stand after that. \n

The goal of the game is to get as close to or exactly to the value of 21, without exceeding it.
Whoever gets closest without busting (going over 21) wins. If you win, you double your bet, 
if you loose, well, you loose your bet. \n
All cards have specific values that they correspond with:\n
\t - All number cards are worth their value (eg. a 2 is 2 points, a 7 is 7 points)\n
\t - All face cards (Jack, Queen, King) are worth 10 points\n
\t - An Ace can either be worth 1 or 11 points, whichever is more favorable for you.\n

The best hand is a natural blackjack, which is an Ace and one other card worth 10 points. It can not be beat 
by any other combination of cards, even if they amount to 21 as well.\n
The game ends when you have not enough money to bet again
or you decide to end the round. Either way, the game will let you know how you did in the end.
"""

def pull_a_card(deck_of_cards):
    index = random.randint(0, len(deck_of_cards)-1)
    keys_list = list(deck_of_cards)
    card_key = keys_list[index]
    return card_key

def get_card_value (card_key, deck_of_cards):
    card_value = deck_of_cards[card_key]
    return card_value

class Bank():
    def __init__(self):
        self.starting_amount = 0
        self.minimum_bet = 0
        self.maximum_bet = 0
        self.balance = 0
    # Gets player input for the starting amount and makes sure the input is valid
    def set_starting_amount(self):
        self.starting_amount = input("Great, lets begin. Minimum buyin is 100$, the maximum is 10.000$. How much money would you like to start with? ")
        self.starting_amount = int(self.starting_amount)
        if type(self.starting_amount) is not int:
            self.starting_amount = input("Please enter a number between 100 and 10000 without decimals or extra signs: ")
        while self.starting_amount < 100 or self.starting_amount > 10000:
            self.starting_amount = input("Minimum buyin is 100$, the maximum is 10.000$. How much money would you like to start with? ")
        return self.starting_amount

    def set_initial_balance(self, starting_amount):
        self.balance = self.starting_amount
        return self.balance

    # keeps track of current player balance
    def balance_tracker():
        return
    # Calculates the bet sizes based on the starting amount
    def set_bet_size(self, starting_amount):
        self.minimum_bet = self.starting_amount // 100
        self.maximum_bet = self.starting_amount // 10
        return self.minimum_bet, self.maximum_bet

    def show_player_balance(self, balance, minimum_bet, maximum_bet):
        return "Your current balance is " + str(self.balance) + "$. The minimum bet is " + str(self.minimum_bet) + "$, the maximum is " + str(self.maximum_bet) + "$."

class Mechanics():
    ### This class handles game mechanics ###

    # Selects a card at random and returns the card name
    def pull_a_card(deck_of_cards):
        index = random.randint(0, len(deck_of_cards)-1)
        keys_list = list(deck_of_cards)
        card_key = keys_list[index]
        return card_key

    # Determines the corresponding value of a card
    def get_card_value (card_key, deck_of_cards):
        card_value = deck_of_cards[card_key]
        return card_value 


# class Main():
    ### Contains the gameplay loop ###

    #print(intro)
    #While the balance is > minimum bet:
    #Show player his balance
    #Ask player if he would like to continue, see the rules again or stop
    #Ask for bet and check that bet is >= minimum_bet and <= maximum_bet
    #Deal two cards to player and dealer
    #Tell player his cards and one card of dealer
    #Ask if he wants to Hit(h), Stand(s) or Double Down (D)
        # While player_points < 21:
            #Ask player if he wants to Hit(h) or Stand(s)
            # When he stands evaluate Dealer
        # If player_points = 21 and number of cards > 2:
            # evaluate Dealer       
###
new = Bank()
new.set_starting_amount()
new.set_initial_balance(new.starting_amount)
new.set_bet_size(new.starting_amount)
print(new.show_player_balance(new.balance, new.minimum_bet, new.maximum_bet,))
#Bank.show_player_balance()
# Card Value check
# print (get_card_value(new_card, deck_of_cards))



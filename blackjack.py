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


class Bank():
    def __init__(self):
        self.starting_amount = 0
        self.minimum_bet = 0
        self.maximum_bet = 0
        self.balance = 0
    # Gets player input for the starting amount and makes sure the input is valid
    def set_starting_amount(self):
        while True:
            try:
                self.starting_amount = int(input("Minimum buyin is 100$, the maximum is 10.000$. How much money would you like to start with? "))
                while self.starting_amount < 100 or self.starting_amount > 10000:
                    self.starting_amount = input("Minimum buyin is 100$, the maximum is 10.000$. How much money would you like to start with? ")
                    self.starting_amount = int(self.starting_amount)
                break
            except ValueError:
                print("Your input was not a number. Press Enter and try again please.")
        
        return self.starting_amount
    # Sets the balance equal to the starting amaount
    def set_initial_balance(self):
        self.balance = self.starting_amount
        return self.balance

    # keeps track of current player balance
    def balance_tracker():
        return
    # Calculates the bet sizes based on the starting amount
    def set_bet_size(self):
        self.minimum_bet = self.starting_amount // 100
        self.maximum_bet = self.starting_amount // 10
        return self.minimum_bet, self.maximum_bet

    #Display player balance and bet size
    def show_player_balance(self):
        return "Your current balance is " + str(self.balance) + "$. The minimum bet is " + str(self.minimum_bet) + "$, the maximum is " + str(self.maximum_bet) + "$."

class Deck():
    ### This class handles Card mechanics ###
    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards
        self.player_card_one = ""
        self.player_card_two = ""
        self.player_total = 0
        self.dealer_total = 0

    # Selects a card at random and returns the card key
    def pull_a_card(self):
        index = random.randint(0, len(self.deck_of_cards)-1)
        keys_list = list(deck_of_cards)
        card_key = keys_list[index]
        return card_key

    # Determines value of initial 2 player cards
    def player_card_values (self):
        self.player_total = (self.deck_of_cards[self.player_card_one] + deck_of_cards[self.player_card_two])
        return self.player_total 

    # Determines value of initial 2 player cards
    def dealer_card_values(self):
        self.dealer_total = (deck_of_cards[self.dealer_card_one] + deck_of_cards[self.dealer_card_two])
        return self.dealer_total

    # Pull two player cards and two dealer cards, making sure that 4 different cards are pulled
    def draw_new_cards(self):
        self.player_card_one = self.pull_a_card()
        self.player_card_two = self.pull_a_card()
        self.dealer_card_one = self.pull_a_card()
        self.dealer_card_two = self.pull_a_card()
        while self.player_card_one == self.player_card_two:
            self.player_card_two = self.pull_a_card()
        while self.dealer_card_one == self.dealer_card_two or self.dealer_card_one == self.player_card_one:
            self.dealer_card_one = self.pull_a_card()
        return self.player_card_one, self.player_card_two, self.dealer_card_one, self.dealer_card_two

    # Check if either player or dealer have natural blackjack after inital draw
    def check_for_blackjack(self):
        if self.player_total == 21 and self.dealer_total != 21:
            #player gets betsize added to balance
            return "You have a natural Blackjack and win your bet"
        elif self.player_total == 21 and self.player_total == self.dealer_total:
            #player balance is unchanged
            return "You both have a natural blackjack. You receive your bet back"
        elif self.player_total != 21 and self.dealer_total == 21:
            #player looses amount he bet
            return "The dealer has a natural blackjack and wins. You loose your bet"
        else:
            return False


#class Main():
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
### TESTING

#new = Bank()
#new.set_starting_amount() #gets starting amount from player
#new.set_initial_balance() # transform starting amount into balance
#new.set_bet_size() # set bet size based on starting amount
#print(new.show_player_balance()) # tells player balance and bet size

new_deck = Deck(deck_of_cards)
print(new_deck.draw_new_cards()) #draws the player cards and dealer cards
print(new_deck.dealer_card_values())
print(new_deck.player_card_values()) # calculates the player card vaule
print(new_deck.check_for_blackjack())

#print(new_deck.player_card_values(new_deck.player_card_one, new_deck.player_card_two))
# Card Value check
# print (get_card_value(new_card, deck_of_cards))



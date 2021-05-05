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


def pull_a_card(deck_of_cards):
    index = random.randint(0, len(deck_of_cards)-1)
    keys_list = list(deck_of_cards)
    card_key = keys_list[index]
    return card_key

def get_card_value (card_key, deck_of_cards):
    card_value = deck_of_cards[card_key]
    return card_value

new_card = pull_a_card(deck_of_cards)
print (get_card_value(new_card, deck_of_cards))



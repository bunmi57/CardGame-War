#Suit,Rank,Value

import random
#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Card Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# two_hearts = Card("Hearts", "Two")
# three_of_clubs = Card("Clubs", "Three")
# print(three_of_clubs.value)
# print(two_hearts.value == three_of_clubs.value)

#Deck Class
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self): #dels one card 
        return self.all_cards.pop()

# new_deck = Deck()
# new_deck.shuffle()
# mycard = new_deck.deal_one()
# print(mycard)
# print(len(new_deck.all_cards))
# mycard = new_deck.deal_one()
# print(mycard)
# print(len(new_deck.all_cards))

# first_card = new_deck.all_cards[-1]
# print(first_card)
# new_deck.shuffle()
# print(new_deck.all_cards[0])
# for card_object in new_deck.all_cards:
#     print(card_object)
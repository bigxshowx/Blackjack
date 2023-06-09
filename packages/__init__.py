import random

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,
          "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":(1,11)}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
          "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Bankroll():

    def __init__(self, amount):
        self.balance = 100
        self.amount = amount

    def deposit(self):
        self.balance += amount



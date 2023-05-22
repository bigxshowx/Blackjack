from packages import *

'''Need classes for a deck, human player, bankroll for bets:
1- Dealer 1 up and one down for self, player 2 cards up
2- Actions to stay or hit only, ignore others (split...)
3- each hit sum the card vs. dealer..
4- dealer then hits until
5 - win (money goes to player), push, or bust (money goes to dealer..)
'''

new_card = Card("Hearts","Ace")

def ace_dealt(card):
    if card.rank == "Ace":
        choice = None #input('Choose value 1 or 11')
        return choice

print(new_card)
print(new_card.value)

testing = ace_dealt(new_card)

print(testing)

new_deck = Deck()

print(len(new_deck.all_cards))
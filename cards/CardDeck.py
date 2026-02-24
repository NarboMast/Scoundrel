from cards.Card import Card
import random

class CardDeck:
    SUITS = ('clubs', 'hearts', 'spades', 'diamonds')
    VALS = range(2, 15)

    def __init__(self):
        self.card_deck = []
        self.build()

    def build(self):
        for suit in self.SUITS:
             for val in self.VALS:
                 self.card_deck.append(Card(val, suit))

    def get_shuffled_card_deck(self):
        random.shuffle(self.card_deck)
        return self.card_deck
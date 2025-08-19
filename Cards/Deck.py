import random
from .Card import Card


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["clubs", "diamonds", "hearts", "spades"]


class Deck:
    def __init__(self):
        self.deck = [Card(x, y) for x in ranks for y in suits]

    def all_deck(self):
        for x in self.deck:
            print(x)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        take_card = self.deck.pop()
        return take_card

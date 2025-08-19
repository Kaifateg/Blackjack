import sys
from .Player import Player
from logger import logger


sys.path.append("..")


class Dealer(Player):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def __str__(self):
        dealer_hand = ""
        for x in self.hand:
            dealer_hand += str(x)+", "
        return f"___dealer’s start hand: ({dealer_hand.rstrip(', ')})"

    @staticmethod
    def dealer_move(dealer, player, deck, player_chips):
        if dealer.get_value() < 17:
            dealer.hit(deck.deal())
            message = (f"DEALER’S MOVE: Hit\n{player_chips.get_bet()}\n"
                  f"{player}\n{dealer}")
            logger(message)
        else:
            dealer.option = "stand"
            message = (f"DEALER’S MOVE: Stand\n"
                  f"{player_chips.get_bet()}\n{player}\n{dealer}")
            logger(message)

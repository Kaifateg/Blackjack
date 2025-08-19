from Cards.Deck import Deck
from Players.Player import Player
from Players.Dealer import Dealer
from Chip import Chip
from result import result
from logger import logger


with open("blackjacklog.txt", "w", encoding="utf-8") as file:
    pass

player_chips = Chip()


while True:
    if player_chips.total == 0:
        message = f"Game over. No chips"
        logger(message)
        break
    while True:
        player = Player()
        dealer = Dealer()
        deck = Deck()
        deck.shuffle()
        player.hit(deck.deal())
        player.hit(deck.deal())
        dealer.hit(deck.deal())
        message = f"***Start blackjack game***"
        logger(message)
        player.player_bet(player_chips, player, dealer)
        if player.get_value() == 21 and len(player.hand) == 2:
            player_chips.player_won()
            message = (f"***Game finish***\nRESULTS:\n___player: "
                       f"{player.get_value()} (blackjack)\n___dealer: "
                       f"{dealer.get_value()}\n___player won")
            logger(message)
            break
        else:
            while not (player.option == "stand" and dealer.option == "stand"):
                if not dealer.option == "stand":
                    dealer.dealer_move(dealer, player, deck, player_chips)
                if not player.option == "stand":
                    player.player_move(player, deck, dealer, player_chips)
            result(player, dealer, player_chips)
            break

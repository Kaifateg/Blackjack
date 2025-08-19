import sys
from logger import logger


sys.path.append("..")

values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
          "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.option = "hit"
        self.hand = []
        self._value = 0
        self.ace = 0

    def __str__(self):
        player_hand = ""
        for x in self.hand:
            player_hand += str(x)+", "
        return f"___player’s start hand: ({player_hand.rstrip(', ')})"

    def get_value(self):
        return self._value

    def hit(self, card):
        self.hand.append(card)
        self._value += values[card.rank]
        if card.rank == "A":
            self.ace += 1
        while self._value > 21 and self.ace > 0:
            self._value -= 10
            self.ace -= 1

    @staticmethod
    def double_down(func_double_bet, func_hit):
        return func_double_bet, func_hit

    @staticmethod
    def player_bet(player_bet, player, dealer):
        while True:
            try:
                player_bet.bet = int(input("PLAYER’S BET: "))
                with open("blackjacklog.txt", "a") as file:
                    file.write("PLAYER’S BET: " + str(player_bet.bet) + "\n")
            except Exception:
                message = (f"Error. WRONG INPUT:\n___player’s bet must be "
                      f"positive integer\nTRY AGAIN.")
                logger(message)
            else:
                if player_bet.bet > player_bet.total:
                    message = (f"Error. You don't have enough chips. Your "
                               f"chips: {player_bet.get_total()}")
                    logger(message)
                elif player_bet.bet <= 0:
                    message = (f"Error. WRONG INPUT:\n___player’s bet must be "
                          f"positive integer\nTRY AGAIN.")
                    logger(message)
                else:
                    message = f"{player_bet.get_bet()}\n{player}\n{dealer}"
                    logger(message)
                    break

    @staticmethod
    def player_move(player, deck, dealer, player_chips):
        move = ["hit", "stand", "double down"]
        if player.get_value() <= 21 and not player.option == "stand":

            while True:
                try:
                    player.option = str(input("PLAYER’S MOVE: ")).lower()
                    with open("blackjacklog.txt", "a") as file:
                        file.write("PLAYER’S MOVE: " + player.option + "\n")
                except Exception:
                    message = (f"Error. WRONG INPUT:\n___player’s move must "
                          f"be one string: hit, stand, double_down)")
                    logger(message)
                else:
                    if (player.option == "double down" and player_chips.bet*2 >
                            player_chips.total):
                        message = (f"Error. You don't have enough chips. "
                                   f"Your chips: {player_chips.get_total()}")
                        logger(message)
                    elif player.option in move:
                        break
                    else:
                        message = (f"Error. WRONG INPUT:\n___player’s move "
                              f"must be one string: hit, stand, double down)")
                        logger(message)

            if player.option == "hit":
                player.hit(deck.deal())
                message = f"{player_chips.get_bet()}\n{player}\n{dealer}"
                logger(message)
            elif player.option == "double down":
                player.double_down(player_chips.double_bet(),
                                   player.hit(deck.deal()))
                message = f"{player_chips.get_bet()}\n{player}\n{dealer}"
                logger(message)
            else:
                message = f"{player_chips.get_bet()}\n{player}\n{dealer}"
                logger(message)
        else:
            player.option = "stand"

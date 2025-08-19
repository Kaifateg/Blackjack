from logger import logger


def result(player, dealer, player_chips):
    if player.get_value() > 21 and dealer.get_value() > 21:
        player_chips.draw()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()} (bust)\n"
              f"___dealer: {dealer.get_value()} (bust)\n___draw")
        logger(message)
    elif player.get_value() == dealer.get_value():
        player_chips.draw()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()}\n"
              f"___dealer: {dealer.get_value()}\n___draw")
        logger(message)
    elif player.get_value() > dealer.get_value() and (player.get_value() <
                                                      22 and
                                                      dealer.get_value() < 22):
        player_chips.player_won()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()}\n"
              f"___dealer: {dealer.get_value()}\n___player won")
        logger(message)
    elif player.get_value() < 22 and dealer.get_value() > 21:
        player_chips.player_won()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()}\n"
              f"___dealer: {dealer.get_value()} (bust)\n___player won")
        logger(message)
    elif player.get_value() > 21 and dealer.get_value() < 22:
        player_chips.player_lost()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()} (bust)\n"
              f"___dealer: {dealer.get_value()}\n___player lost")
        logger(message)
    else:
        player_chips.player_lost()
        message = (f"***Game finish***\nRESULTS:\n"
              f"___player: {player.get_value()}\n"
              f"___dealer: {dealer.get_value()}\n___player lost")
        logger(message)

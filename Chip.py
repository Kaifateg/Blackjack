class Chip:
    def __init__(self, total=100, bet=0):
        self.total = total
        self.bet = bet

    def get_total(self):
        return self.total

    def get_bet(self):
        return f"___player’s bet: {self.bet} chips"

    def player_won(self):
        self.total += self.bet

    def player_lost(self):
        self.total -= self.bet

    def draw(self):
        self.bet = 0

    def double_bet(self):
        self.bet *= 2

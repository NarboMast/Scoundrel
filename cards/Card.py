class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        return f"{self.val} of {self.suit}"
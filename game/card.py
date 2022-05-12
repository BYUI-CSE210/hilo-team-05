import random


class Card:
    """A card with a different number in each one.

    The responsibility of Card is to keep track of the numbers of
    the get cards; it coul be the current card and the card to guess.

    Attributes:
        value (int): The number of the both cards, the current card and
        the card to guess.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = 0
        self.card_to_guess = 0

    def get_cards(self):
        """Generates two randoms of numbers to generate the number of
        the current card and the number of the next card(card to guess)

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = random.randint(1, 13)
        self.card_to_guess = random.randint(1, 13)

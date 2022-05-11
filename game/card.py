import random


class Card:
    """A card with a different number in each one.

    The responsibility of Card is to keep track the number of current card,
    and the number of the next card

    Attributes:
        value (int): The number of the current card and the next card
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = 0
        self.card_to_guess = 0
        self.higher_lower = ""

    def get_cards(self):
        """Generates a new random values for the current card and for the 
        next card. It also tracks if it is higher or lower.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = random.randint(1, 13)
        self.card_to_guess = random.randint(1, 13)
        if self.current_card < self.card_to_guess:
            self.higher_lower = "h"
        else:
            self.higher_lower = "l"

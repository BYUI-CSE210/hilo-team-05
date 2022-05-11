from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Card (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        card_current (int): is the number of first card.
        second:card (int): is the number of the second card to guess.
        points (int): The score for one round of play.
        ask_guess (str): Is the answer in the input of the guess
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.cards = Card()
        self.card_current = 0
        self.second_card = 0
        self.points = 300
        self.ask_guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_current_card()
            self.get_second_card()
            self.guess_card()
            self.get_play_again()

        print("Thank you for playing!")

    def get_current_card(self):
        """Here we saved in the first self.card_current variable
        the current card generated in card.py 
        """
        self.cards.get_cards()

        self.card_current = self.cards.current_card

        print(f"The card is: {self.card_current}")

    def get_second_card(self):
        """Here we saved in the first self.second_card variable
        the card_to_guess card generated in card.py 
        """
        self.ask_guess = input("Higher or lower? [h/l] ")
        self.second_card = self.cards.card_to_guess

        print(f"the next card was: {self.second_card}")

    def guess_card(self):
        """Here the program manage two options in the random 
        generated, the cards could be equal or not. If are
        equal show message, but if not, the answer could be true 
        or false, so the gamer coul loose points io gain points. 
        """
        if self.second_card == self.card_current:
            print("The two cards are the same")

        else:

            if self.ask_guess == "h":
                is_true = (self.second_card > self.card_current)

            elif self.ask_guess == "l":
                is_true = (self.second_card < self.card_current)

            if is_true == False:
                self.points -= 75
            else:
                self.points += 100

        print(f"Your score is: {self.points}")
        print()

    def get_play_again(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")

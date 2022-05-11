<<<<<<< HEAD

from game.card import Card
=======
from game.card import Card
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""
>>>>>>> b0f5c896bea9fe13b6b1ca5c532bcc813d2f7864


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Card (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
<<<<<<< HEAD
        self.cards = Card()
        self.card_current = 0
        self.second_card = 0
        self.points = 300
        self.ask_guess = ""
=======
        self.score = 300
        self.win = None
>>>>>>> b0f5c896bea9fe13b6b1ca5c532bcc813d2f7864

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

<<<<<<< HEAD
    def get_current_card(self):
        """"""
        self.cards.get_cards()
=======
        Args:
            self (Director): An instance of Director.
        """
        card = Card()
        card.get_cards()

        print(f"\nThe card is: {card.current_card}")
        choice = input("Higher or lower? [h/l] ")
        print(f"Next card was: {card.card_to_guess}")

        if choice == card.higher_lower:
            self.win = True
        else: self.win = False
>>>>>>> b0f5c896bea9fe13b6b1ca5c532bcc813d2f7864

        self.card_current = self.cards.current_card

<<<<<<< HEAD
        print(f"The card is: {self.card_current}")

    def get_second_card(self):
        self.ask_guess = input("Higher or lower? [h/l] ")
        self.second_card = self.cards.card_to_guess

        print(f"the next card was: {self.second_card}")

    def guess_card(self):
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
=======
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if self.win == True:
            self.score += 100
        else: self.score -= 75

        print(f"Your score is: {self.score}")
>>>>>>> b0f5c896bea9fe13b6b1ca5c532bcc813d2f7864

    def get_play_again(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
<<<<<<< HEAD
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")
=======
        if not self.is_playing:
            return

        if self.score > 0:
            play = input("Play again? [y/n] ")

            if play == "n":
                self.is_playing = False
        else: 
            self.is_playing = False
            print("You lost all of your points, good luck next time!")
        
>>>>>>> b0f5c896bea9fe13b6b1ca5c532bcc813d2f7864

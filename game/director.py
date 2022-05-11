from game.card import Card
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""


class Director:
    """"""
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.win = None

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

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

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if self.win == True:
            self.score += 100
        else: self.score -= 75

        print(f"Your score is: {self.score}")

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        if self.score > 0:
            play = input("Play again? [y/n] ")

            if play == "n":
                self.is_playing = False
        else: 
            self.is_playing = False
            print("You lost all of your points, good luck next time!")
        

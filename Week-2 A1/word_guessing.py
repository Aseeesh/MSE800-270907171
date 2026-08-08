import random


class WordGuessingGame:
    # Defined as a class attribute so display_hangman can access it
    HANGMAN_PICS = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\ |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\ |
          /    |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\ |
          / \\  |
               |
         ========="""
    ]

    def __init__(self, lives=6):
        """Constructor: Initializes words, game variables, and lives."""
        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        self.secret_word = random.choice(words)
        self.blanks = ["_"] * len(self.secret_word)
        self.max_lives = lives  # Fixed: Saved total lives so stage_index math works
        self.lives = lives
        self.used_letters = set()

    def display_hangman(self):
        """Prints the hangman stage matching the current lives used."""
        stage_index = self.max_lives - self.lives
        print(self.HANGMAN_PICS[stage_index])

    def get_valid_guess(self):
        """Asks for input and uses try-except for input validation."""
        while True:
            try:
                guess = input("Guess a letter: ").strip().lower()

                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError("Please enter a single letter (A-Z).")
                if guess in self.used_letters:
                    raise ValueError("You already guessed that letter.")

                return guess
            except ValueError as error:
                print(f"  → {error}")

    def play(self):
        """Runs the main game loop."""
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        # Loop until won or out of lives
        while self.lives > 0 and "_" in self.blanks:
            guess = self.get_valid_guess()
            self.used_letters.add(guess)

            if guess in self.secret_word:
                # Reveal correct guesses
                for i, char in enumerate(self.secret_word):
                    if char == guess:
                        self.blanks[i] = guess
                print("\nNice job! You found a letter.")
            else:
                self.lives -= 1
                self.display_hangman()
                print(f"\nWrong guess! Lives left: {self.lives}")

            print(" ".join(self.blanks))

        # Check win/loss state
        if "_" not in self.blanks:
            print(f"\nCongratulations! You won! The word was: {self.secret_word}")
        else:
            print(f"\nGame Over! Out of lives. The word was: {self.secret_word}")


def main():
    """Main entry point for the game."""
    try:
        game = WordGuessingGame(lives=6)
        game.play()
    except KeyboardInterrupt:
        print("\nGame closed by user.")


if __name__ == "__main__":
    main()
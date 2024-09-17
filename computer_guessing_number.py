import random


class NumberGuesser:
    def __init__(self):
        """Initialize the game with default values"""
        self.low = 1    # Lower bound for guessing
        self.high = 100 # Upper bound for guessing
        self.guesses = 0    # Track number of guesses
        self.my_number = int(input('Enter a number from 1 to 100 then I will try to guess it ok? '))
        self.computer_choice = random.randint(self.low, self.high)  # Computer's first guess

    def update_guess_range(self, direction):
        """Update the guessing range based on user's input (higher or lower)"""
        if direction == 'Higher':
            self.low = self.computer_choice # Use self to refer to the class attribute
            self.computer_choice = random.randint(self.low + 1, self.high)  # Narrowing the range
        elif direction == 'Lower':
            self.high = self.computer_choice
            self.computer_choice = random.randint(self.low, self.high - 1)  # Narrowing the range
        self.guesses += 1   # Increment the guess counter

    def play(self):
        """Main game loop where the computer guesses the number"""
        while self.my_number != self.computer_choice:
            print(f'My total guesses: {self.guesses}')
            print(f'Hmm, I choose {self.computer_choice}. Higher or lower?')
            guess = input(': ').capitalize()

            if guess in ['Higher', 'Lower']:
                self.update_guess_range(guess)  # Update the range based on user input
            else:
                print('Invalid input. Please enter "Higher" or "Lower".')

        print(f'Yes! It was {self.my_number}! I guessed it after {self.guesses} tries!')


# Start the game
if __name__ == '__main__':
    game = NumberGuesser()
    game.play()
    stop = input(" ")

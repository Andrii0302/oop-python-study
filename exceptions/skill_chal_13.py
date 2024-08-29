from random import choice
from string import ascii_lowercase
import time
from collections import defaultdict
# letters=ascii_lowercase
# should_run=True
# picked=choice(letters)
# print(picked)
# while should_run:
#     try:
#         guess=input()
#         if guess not in letters:
#             raise ValueError
#     except ValueError:
#         print('Given Invalid letter ')
#         try:
#             answer=input('Do you want to continue? Y/N\n').upper()
#             if answer not in ('Y', 'N'):
#                 raise ValueError
#         except (ValueError,KeyboardInterrupt):
#             should_run=False
#         else:
#             if answer == 'N':
#                 should_run=False
#     else:
#         if guess == picked:
#             print(f"You've guessed a letter - {picked}")
#             should_run=False
#         else:
#             continue

class LetterGuessingException(Exception):
    """The exception base class for the LetterGuessing game."""
class LetterComesAfter(LetterGuessingException):
    pass
class LetterComesBefore(LetterGuessingException):
    pass
class NotALetter(LetterGuessingException):
    pass
class LetterGuessingGame:
    def __init__(self):
        self.start_time = time.time()
        self.performance = defaultdict(list)
        self._correct_guess=False
    def _display_performance(self):
        time_taken= time.time() - self.start_time
        return f"{'That was correct!' if self._correct_guess else 'Game interrupted.'} Total time taken: {round(time_taken,2)} seconds and made {len(self.performance['before']) + len(self.performance['after'])} guesses."
    @staticmethod
    def pick():
        print('The computer has chosen a letter')
        return choice(list(ascii_lowercase))
    @staticmethod
    def _validate_user_input(computer_choice, user_guess):
        if user_guess not in list(ascii_lowercase):
            raise NotALetter
        elif user_guess < computer_choice:
            raise LetterComesAfter
        elif user_guess > computer_choice:
            raise LetterComesBefore
        print('You are gay and I am gay')
        return True
    def play(self):
        computer_choice=self.pick()
        user_guess=None
        while True:
            try:
                user_guess=input().strip().lower()
                self._validate_user_input(computer_choice,user_guess)
                self._correct_guess = True
                break
            except LetterComesAfter:
                print('The letter you have entered comes after the computer\'s choice')
                self.performance['before'].append(user_guess)
            except LetterComesBefore:
                print('The letter you have entered comes before the computer\'s choice')
                self.performance['after'].append(user_guess)
            except NotALetter:
                print('The thing you have entered is not a letter')
            except KeyboardInterrupt:
                print(self._display_performance())
        print(self._display_performance())
if __name__ == "__main__":
    game=LetterGuessingGame()
    game.play()
            

            

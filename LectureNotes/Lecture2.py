from IPython.display import clear_output
import random
class WordGuessing:
    def __init__(self, secret):
        '''
        This object gets player guess and checks its correctness.
        It also is used to display the "_ _ X _ X _" word status

        Parameter:
        ---------
        secret = word to guess, must be cleaned already (stripped, lowered, etc)
        '''

        self.secret = secret.strip().lower() # secret word to be guessed
        self.guesses = []# list of all guess chars
        self.correct_guesses = ["_"] * len(self.secret)# list of blanks characters to be replaced with correct car

    def _update_correct_guesses(self, guess_char):
        '''
        Puts guess_char into the correct position in the self.correct_guesses list
        '''
        for i, char in enumerate(self.secret):
            if char == guess_char:
                self.correct_guesses[i] = guess_char

        

    def check_guess(self, guess_char):
        '''
        Gets player guess and checks its correctness.

        Parameter:
        ---------
        guess_char = cleaned character guess (stripped, lowered, etc)

        Returns:
        ------
        "wrong" = if guess is wrong...
        "repeat" = repeat guess
        "correct" = correct guess
        "success" = all letters successfully guessed
        '''
        if (guess_char in self.guesses):
          return "repeat"
       
        elif (guess_char in self.secret):
          self.guesses.append(guess_char)
          self._update_correct_guesses(guess_char)
          if ("_" not in self.correct_guesses):
            return "success"
          return "correct"
        else:
          self.guesses.append(guess_char)
          return "wrong"
          

        # first check if it's already been guessed, otherwise append to guesses

        # then check if it's correct or not
            # after updating word status, check if it's been completely guessed
            # return 'success' or 'correct' accdgly
        # otherwise wrong guess

    def display_word(self):
        print("Word: " + " ".join(self.correct_guesses).upper()) # Word: _ _ X _ ...


class TextInterface:
    def __init__(self):
        self.stages = [
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
             ========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
             ========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
             ========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
             ========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
             ========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
             ========
            """,
            """
               -----
               |   |
                   |
                   |
                   |
                   |
             ========
            """,
        ]
        # input strings into the list so that you get different messages
        # when you call self.display_message()
        self.messages = {
            "start" : ["Welcome to Hangman. Guess one letter at a time to uncover the whole word. Just don't get too many answers wrong...","This is Hangman, where every guess puts a man's life on the line... literally.","HANGMAN START! I won't leave you hanging, so let the guessing begin!"],
            "correct" : ['Correct!','You got it!','Great job!'],
            "wrong" : ['Wrong.',"That letter isn't in the word.","Incorrect guess."],
            "repeat" : ['You already used this letter.','Try something else next time.','You guessed this before already!'],
            "success" : ['You win!','Congratulations, you guessesd the whole word!','You got everything before the man could be hanged, phew!'],
            "end" : ['Game over.','Too many mistakes. You lose.',"Womp womp- I mean oh no, the man got hanged!!"],
        }

    def display_hangman(self, lives_left):
        print(self.stages[lives_left])

    def display_message(self, status):
        '''
        Generate game message

        Parameters
        ----------
        status = one of: "start", "correct", "wrong", "repeat", "success", "end"
        '''
        m_grp = self.messages[status]
        print("\n" + m_grp[random.randint(0,len(m_grp)-1)])

class GameLogic: #GAME LOGIC
    def __init__(self):
        '''
        This object will run the hangman gameplay. It keeps track of the lives,
        displays all interface, and gets user input.
        '''
        self.lives_left = 6 # how many lives?
        self.guess_status = "start" # what should be the initial value
        self.word_bank = ["python","apple","banana","coding","programming","joserizal"]# words to guess
        self.Word = WordGuessing(self._generate_word_to_guess()) # use WordGuessing Object
        self.TUI = TextInterface() # use TextInterface Obect

    def _generate_word_to_guess(self):
        # code here
        secret = random.choice(self.word_bank)
        return secret

    def _display_all_interface(self):
        # code here, clear the output, display hangman, display word status, and display message
        clear_output()  # clears the screen
        self.TUI.display_hangman(self.lives_left)  # display hangman based on lives left
        self.Word.display_word()  # display the current word status (_ _ _ _ _)
        self.TUI.display_message(self.guess_status)  # display the message related to the guess

    def _get_user_input(self):
        # code here, lower and strip the character input
        guess = input("Guess a character").strip().lower()
        return guess

    def play(self):

        # start iterative game
        while self.lives_left > 0 and not self.guess_status == "success":
            # display interface
            self._display_all_interface()
            # get input
            guess = self._get_user_input()

            # process user input using Word
            self.guess_status = self.Word.check_guess(guess)

            # decide what to do next based on guess_status
            if self.guess_status == 'wrong':
              self.lives_left -= 1  # Lose a life if the guess is wrong
            elif self.guess_status == "correct":
            # Check if the player has won by guessing all letters
              if "_" not in self.Word.correct_guesses:
                self.guess_status = "success"
                break
            elif self.guess_status == "repeat":
              continue  # Skip turn if the guess is repeated

        # conclude the game
        if self.lives_left == 0:
            self.guess_status = "end"  # Set the game status to end if lives run out
            self._display_all_interface()  # Update interface
        else:
            self.guess_status = "success"  # Set the game status to success if word is fully guessed
            self._display_all_interface()
        # update interface
        print("The correct word is:", self.Word.secret)


game = GameLogic()
game.play()



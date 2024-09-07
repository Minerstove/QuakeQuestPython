import random
import time

def generate_word_to_guess() -> str:
  mystery = ["python", "code", "syntax", "program"]
  unknown = random.choice(mystery)
  return unknown

def get_user_guess() -> str:
  u_input = input("input any letter: ").strip().lower()
  return u_input


def print_hangman(num_wrong_guesses: int) -> None:
    # clear_output, then print hangman figure in google colab
     hangman = [
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
        /|\  |
             |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========""",
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========""",
    ]
     print(hangman[num_wrong_guesses])




def check_answer(num_wrong_guesses: int,correct_word: str,user_answer: str,guessed_letters: set,correct_guesses: list) -> int:
    if user_answer  in guessed_letters:
        print("you already guessed that")
        time.sleep(2)        
    elif user_answer in correct_word:
        print("You guessed correctly!")
        guessed_letters.append(user_answer)
        for i, letter in enumerate(correct_word):
            if user_answer == letter:
                correct_guesses[i] = user_answer
    else:
        print("you fuckigng failure")
        time.sleep(2)
        guessed_letters.append(user_answer)
        num_wrong_guesses +=1
    return num_wrong_guesses

def main():
    # Define fixed variables
    WORD = generate_word_to_guess()
    MAX_WRONG = 6


    # Define variables that will change throughout the game
    num_wrong_guesses = 0
    guessed_letters = []
    correct_guesses = ["_"] * len(WORD)


    while True:
        # Print first scenario: no hangman, show current word in blanks,
        print_hangman(num_wrong_guesses)
        print("Current word:", " ".join(correct_guesses))


        # Get user input, check that input
        user_answer = get_user_guess()
        num_wrong_guesses = check_answer(num_wrong_guesses, WORD, user_answer, guessed_letters, correct_guesses)


        # Before proceeding to next iteration, check if player have already guessed correctly
        if "_" not in correct_guesses:
            print("Congratulations, you've guessed the word:", WORD)
            break


        # The not yet guessed, then check naman the num of wrong guesses
        if num_wrong_guesses >= MAX_WRONG:
            print_hangman(num_wrong_guesses)
            print(f"Sorry, you've been hanged! The word was: {WORD}")
            break
main()

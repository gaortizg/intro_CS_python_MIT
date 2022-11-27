# Hangman Game
# -----------------------------------
import random
import string

# Define name of file as a global variable
WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# main function 
# -----------------------------------
def main():
  # Load the list of words into the variable wordlist
  wordlist = load_words()

  # Set 'secret_word' manually
  # secret_word = "dolphin"

  # Randomly choose 'secret_word' to guess
  secret_word = choose_word(wordlist)

  # Run hangman program
  hangman(secret_word)

# -----------------------------------
# load_words function 
# -----------------------------------
def load_words():
    '''
    Input:
    None (void function)

    Returns:
    List of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while
    to finish.
    '''
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(f"{len(wordlist)} words loaded.")
    return wordlist

# -----------------------------------
# choose_word function 
# -----------------------------------
def choose_word(wordlist):
    '''
    Input:
    wordlist (list): list of words (strings)

    Returns:
    A word from 'wordlist' at random
    '''
    return random.choice(wordlist)

# -----------------------------------
# is_word_guessed function 
# -----------------------------------
def is_word_guessed(secret_word, letters_guessed):
    '''
    Input:
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far

    Returns:
    boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    '''
    # Check whether each letter in 'secret_word' is in 'letters_guessed'
    check_word = True
    for letter in secret_word:
      if letter not in letters_guessed:
        check_word = False
        break
    
    return check_word

# -----------------------------------
# get_guessed_word function 
# -----------------------------------
def get_guessed_word(secret_word, letters_guessed):
    '''
    Input:
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far

    Returns: 
    string, comprised of letters, underscores (_), and spaces that represents
    which letters in 'secret_word' have been guessed so far.
    '''
    length_word = len(secret_word)
    guessed_letters = list("_" * length_word)

    # loop through each letter in 'letters_guessed'
    for letter in letters_guessed:
      # Loop through each letter in 'secret_word'
      for i in range(length_word):
        if letter == secret_word[i]:
          guessed_letters[i] = letter

    # Concatenate letters into a single string
    final_guess = ""
    for letter in guessed_letters:
      if letter == "_":
        final_guess += "_ "
      else:
        final_guess += letter

    # print final guess
    return final_guess

# -----------------------------------
# get_available_letters function 
# -----------------------------------
def get_available_letters(letters_guessed):
    '''
    Input:
    letters_guessed: list (of letters), which letters have been guessed so far
    
    Returns:
    string (of letters), comprised of letters that represents which letters have
    not yet been guessed.
    '''
    remain_letters = string.ascii_lowercase
    for letter in letters_guessed:
      remain_letters = remain_letters.replace(letter.lower(), '')
    return remain_letters

# -----------------------------------
# hangman function 
# -----------------------------------
def hangman(secret_word):
    '''
    Input:
    secret_word: string, the secret word to guess.
    
    This routine starts up an interactive game of Hangman.
    '''
    # Print welcome message
    print("Welcome to the game Hangman!")
    
    # Compute length of word to guess
    len_word = len(secret_word)
    print(f"I'm thinking of a word that is {len_word} letters long")
    
    # Initialize variables and print info on screen
    warning_input = 3       # Number of warnings
    attempts = 6            # Number of guesses
    my_letters = string.ascii_lowercase
    letters_guessed = []
    print(f"You have {warning_input} warnings left.")

    while attempts > 0:
      # Print info on screen
      print("-" * 13)
      print(f"You have {attempts} guesses left.")
      print(f"Available letters: {my_letters}")

      # Ask user for a letter
      guess = input("Please guess a letter: ")

      # If wrong input
      if (len(guess) > 1) or not(guess.isalpha()):
        # If there are warnings left, decrease number of warnings
        if warning_input > 0:
          warning_input -= 1
          print(f"Oops! That is not a valid letter. You have {warning_input} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        # If no warnings left, decrease number of guesses
        elif attempts >= 2:
          attempts -= 1
          print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        # If no more guesses left, end game
        else:
          print("-" * 13)
          print(f"Sorry, you ran out of guesses. The word was: {secret_word}.")
          break
      
      # If right input
      else:
        # Make sure input is in lowercase
        guess = guess.lower()

        # If letter has already been guessed
        if guess in letters_guessed:
          # If there are warnings left, decrease number of warnings
          if warning_input > 0:
            warning_input -= 1
            print(f"Oops! You've already guessed that letter. You have {warning_input} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
          # If no warnings left, decrease number of guesses
          elif attempts >= 2:
            attempts -= 1
            print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
          # If no more guesses left, end game
          else:
            print("-" * 13)
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break
        
        # If letter has not ben guessed yet
        else:
          # Update list of letters that have already been guessed
          letters_guessed.append(guess)

          # Remove letter from list of available letters
          my_letters = get_available_letters(letters_guessed)

          # If letter does not exist in 'secret_word'
          if guess not in secret_word:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            
            # If letter is a vowel, the user loses two guesses, otherwise, the user loses only one guess
            if guess in "aeiou":
              attempts -= 2
            else:
              attempts -= 1
            
            # Check whether we have guesses left
            if attempts <= 0:
              print("-" * 13)
              print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
              break

          # If letter is in 'secret_word'
          else:
            # Print guessed word so far on screen
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

            # Check whether 'secret_word' has already been guessed and compute score
            if is_word_guessed(secret_word, letters_guessed):
              # Count number of unique letters in 'secret_word'
              unique_words = len(set(secret_word))
              
              # Compute final score
              final_score = attempts * unique_words

              # print results on screen
              print("-" * 13)
              print("Congratulations, you won!")
              print(f"Your total score for this game is: {final_score}")
              break

# -----------------------------------
# RUN MAIN FUNCTION
# -----------------------------------
if __name__ == "__main__":
  main()
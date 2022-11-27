import math
import random

# -----------------------------------
# Define global variables
# -----------------------------------
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Dictionary with scrabble values for each letter
# -----------------------------------
# Notice I added the wildcard character "*" with value zero, since
# player does not receive points when using wildcards
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# main function
# -----------------------------------
def main():
    word_list = load_words()
    global_score = play_game(word_list)

    # Print total score over all hands
    print("-" * 10)
    print(f"Total score over all hands: {global_score}")

# -----------------------------------
# load_words function
# -----------------------------------
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.

    Input: None

    Returns:
    wordlist: List of available words
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# -----------------------------------
# get_frequency_dict function
# -----------------------------------
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    Input:
    sequence: string or list
    
    Returns:
    dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# -----------------------------------
# get_word_score function
# -----------------------------------
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    Input:
    word: string
    n: int >= 0

    Returns:
    score: int >= 0
    """
    # Compute length of 'word' and initialize score
    word_length = len(word)
    score = 0

    # Loop through each letter in 'word'
    for letter in word:
        # First component of score (points for letters)
        score += SCRABBLE_LETTER_VALUES[letter.lower()]

    # Second component of score (reward for long words)
    tmp = 7 * word_length - 3 * (n - word_length)
    if tmp > 1:
        score *= tmp
    else:
        score *= 1
    
    # Reurn final score
    return score

# -----------------------------------
# display_hand function
# -----------------------------------
def display_hand(hand):
    """
    Displays the letters currently in the hand. For example:
        display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
        a x x l l l e
    The order of the letters is unimportant.

    Input:
    hand: dictionary (string -> int)

    Returns: None
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=" ")      # print all on the same line
    print()                              # print an empty line

# -----------------------------------
# deel_hand function
# -----------------------------------
def deal_hand(n):
    """
    Returns a random hand containing 'n' lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    Input:
    n: int >= 0
    
    Returns:
    dictionary (string -> int)
    """
    # Initialize dictionary
    hand={}

    # Choose randomly ceil(n/3) vowels
    num_vowels = int(math.ceil(n / 3))
    for i in range(num_vowels):
        # Always give one wildcard in each hand
        if i == 0:
            x = "*"
            hand[x] = hand.get(x, 0) + 1
        else:
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1
    
    # Choose randomly (n - num_vowels) consonants
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    # Random shuffle dictionary so as to avoid showing all vowels or consonants together
    tmp = list(hand.items())
    random.shuffle(tmp)
    hand = dict(tmp)

    # Return hand
    return hand

# -----------------------------------
# update_hand function
# -----------------------------------
def update_hand(hand, word):
    """
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    Input:
    word: string
    hand: dictionary (string -> int)    
    
    Returns:
    dictionary (string -> int)
    """
    # Make copy of 'hand'
    new_hand = hand.copy()

    # Make sure word is in lowercase
    word = word.lower()

    # Loop through each letter in 'word'
    for letter in word:
        # Check whether letter is in 'new_hand'
        if letter in new_hand:
            # Update number of letters in hand
            if new_hand.get(letter) >= 2:
                new_hand[letter] -= 1
            else:
                # If no more letters left in 'new_hand', delete letter from 'new_hand'
                del new_hand[letter]

    return new_hand

# -----------------------------------
# is_valid_word function
# -----------------------------------
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    Input:
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    
    Returns: boolean (True or False)
    """
    # Make copy of 'hand'
    hand_copy = hand.copy()

    # Make sure 'word' is in lowercase
    word = word.lower()

    # Check whether 'word' is composed entirely of letters in 'hand' or not
    for letter in word:
        # If the letter is not in hand, then 'word' is not valid
        if letter not in hand_copy:
            return False
        else:
            # If there are no letters left in hand, then 'word' is not valid
            if hand_copy[letter] == 0:
                return False
            else:
                # Update hand
                hand_copy[letter] -= 1
    
    # If we reached this line, then 'word is entirely composed of letters in 'hand'
    # Time to check whether 'word' is in 'word_list' or not
    
    # Check case for 'word' with wildcard
    if "*" in word:
        # Loop through each vowel and replace wildcard character by a vowel each time
        for vowel in VOWELS:
            # Replace wildcard character by vowel. Store new word in another
            # variable to avoid modifying original word
            word_copy = word.replace("*", vowel)
            
            # Check whether 'word_copy' is in 'word_list'. If that is the case,
            # then 'word_copy' exists
            if word_copy in word_list:
                return True
    
    # If no wildcard, then check whether 'word' is in 'word_list' or not
    elif word in word_list:
        return True
    else:
        return False 

# -----------------------------------
# calculate_handlen function
# -----------------------------------
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    Input:
    hand: dictionary (string-> int)
    
    Returns: int
    """
    hand_length = 0
    # Loop through each key in 'hand'
    for key in hand:
        hand_length += hand[key]
    return hand_length

# -----------------------------------
# play_hand function
# -----------------------------------
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand

    Input:
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    
    Returns: the total score for the hand
    """
    # Keep track of the total score
    total_score = 0

    # Print hand on screen
    print("Current hand: ", end = "")
    display_hand(hand)

    # As long as there are still letters left in the hand:
    hand_length = calculate_handlen(hand)
    while hand_length > 0:
        # Ask user for input
        word = input("Please enter a word or '!!' to indicate you are done: ")

        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                score = get_word_score(word, hand_length)
                total_score += score
                print(f"'{word}' earned {score} points. Total: {total_score} points")
                print()

            # Otherwise, reject invalid word:
            else:
                print("That is not a valid word. Please choose another word.")
                print()
            # Update the user's hand by removing the letters of their word
            hand = update_hand(hand, word)
            hand_length = calculate_handlen(hand)

            # Display current hand
            print("Current hand: ", end = "")
            display_hand(hand)    

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if not(word == "!!"):
        print("Ran out of letters")
    print(f"Total score for this hand: {total_score}")

    # Return the total score
    return total_score


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    If user provides a letter not in the hand, the hand should be the same.
    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    Input:
    hand: dictionary (string -> int)
    letter: string
    
    Returns:
    dictionary (string -> int)
    """
    # Copy hand
    hand_copy = hand.copy()

    # Make sure letter is lowercase
    letter = letter.lower()

    # Extract keys from dictionary (for comparison)
    keys = list(hand.keys())

    # If letter  not in hand, do nothing
    if letter not in hand_copy:
        return hand_copy
    else:
        # Choose random letter
        x = random.choice(VOWELS + CONSONANTS)

        # If random letter exists in dictionary, keep asking
        # for letter until a new letter that is not in the
        # hand has been chosen
        while x in keys:
            x = random.choice(VOWELS + CONSONANTS)

        # Replace letter provided by user by random choice
        hand_copy[x] = hand_copy.pop(letter)
    
    return hand_copy
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    Input:
    word_list: list of lowercase strings

    Returns the total score for the series of hands
    """
    # Ask the user to input a total number of hands. Validate entry
    n_hands = input("Enter total number of hands: ")
    while True:
        try:
            n_hands = int(n_hands)
            if n_hands <= 0:
                n_hands = input("Enter total number of hands: ")
            else:
                break
        except ValueError:
            n_hands = input("Enter total number of hands: ")

    # Global score across all hands
    global_score = 0

    # Counters for number of hands played, substitutions, and replays
    count_hands = 0
    substitution_count = 0
    replay_count = 0

    # Keep playing until all hands are played
    while count_hands < n_hands:
        # Deel hand
        hand = deal_hand(HAND_SIZE)

        # -----------------------------------------------------------
        # The next lines are for testing (based on PSET3 document)
        # hand1 = {'a':1, 'c':1, 'i':1, '*':1, 'p':1, 'r':1, 't':1}
        # hand2 = {'d':2, '*':1, 'l':1, 'o':1, 'u':1, 't':1}
        # if count_hands == 0:
        #     hand = hand1
        # else:
        #     hand = hand2
        # -----------------------------------------------------------
        
        # Print initial hand on screen
        if (count_hands == 0) or (substitution_count == 0):
            print("Current hand: ", end = "")
            display_hand(hand)

        # Ask user if (s)he wants to substitute one letter for another
        # It can only be done once per game
        if substitution_count == 0:
            ans_sub = input("Would you like to substitute a letter? ")
            
            # Keep asking whether the user wants to substitute a letter
            # until a valid answer is given
            while ans_sub.lower() not in ["y", "yes", "n", "no"]:
                ans_sub = input("Would you like to substitute a letter? ")
            
            # If user wants to do a substitution
            if ans_sub.lower() in ["yes", "y"]:
                letter_to_replace = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter_to_replace)
                substitution_count += 1
        
        # Print empty line
        print()

        # Play a hand
        score = play_hand(hand, word_list)
        print("-" * 10)
        
        # Ask user if they want to replay hand (only if not used before)
        if replay_count == 0:
            replay = input("Would you like to replay the hand? ")

            # Keep asking whether the user wants to replay the hand
            # until a valid answer is given
            while replay.lower() not in ["y", "yes", "n", "no"]:
                replay = input("Would you like to replay the hand? ")

            # If user wnats to replay the hand
            if replay.lower() in ["yes", "y"]:
                replay_count += 1
                substitution_count += 1

                # Repeat hand
                score2 = play_hand(hand, word_list)
                print("-" * 10)

                # Keep better score
                if score2 > score:
                    score = score2

        # Increase counter of hands
        count_hands += 1

        # Update global score
        global_score += score
    
    return global_score

# -----------------------------------
# RUN MAIN FUNCTION
# -----------------------------------
if __name__ == '__main__':
    main()
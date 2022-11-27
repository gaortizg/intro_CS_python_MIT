from scrabble import *
'''
This file contains routines to test the functions created in 'scrabble.py'
'''
# -----------------------------------
# main function
# -----------------------------------
def main():
    # Load list of words
    word_list = load_words()

    # Test 'get_word_score' function
    print("-" * 70)
    print("Testing get_word_score...")
    test_get_word_score()
    
    # Test 'update_hand´ function
    print("-" * 70)
    print("Testing update_hand...")
    test_update_hand()

    # Test 'is_valid_word' function
    print("-" * 70)
    print("Testing is_valid_word...")
    test_is_valid_word(word_list)
    
    # Test 'wildcard' function
    print("-" * 70)
    print("Testing wildcards...")
    test_wildcard(word_list)

    # Let user know all is done
    print("All done!")

# -----------------------------------
# test_get_word_score function
# -----------------------------------
def test_get_word_score():
    """
    Unit test for get_word_score
    """
    success = True
    
    # Dictionary with words to test and their respective scores as follows:
    # { (word, letters_in_hand) : score }
    words = {
        ("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
        ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
        ("fork", 7):209, ("FORK", 4):308
    }

    # Loop through each entry in dictionary
    for (word, n) in words.keys():
        # Compute score using get_word_score function
        score = get_word_score(word, n)
        
        # Check whether score is correct or not
        if not(score == words[(word, n)]):
            print("FAILURE: test_get_word_score()")
            print(f"\tExpected {words[(word, n)]} points but got {score} for word {word}, n = {n}")
            success = False
    
    # If everything goes well, print SUCCESS!!!
    if success:
        print("SUCCESS: test_get_word_score()")

# -----------------------------------
# test_update_hand function
# -----------------------------------
def test_update_hand():
    """
    Unit test for update_hand
    """
    # -----------------------------------
    # Test 1
    # -----------------------------------
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    # Use 'update_hand' function
    hand2 = update_hand(handCopy, word)

    # 'update_hand' can return either one of the following hands
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}

    # Check whether 'update_hand' returns the right answer or not
    if not(hand2 == expected_hand1) and not(hand2 == expected_hand2):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tReturned: {hand2}, \n\t-- but expected: {expected_hand1} or {expected_hand2}")
        return
    
    # Check that we made a copy of original hand
    if not(handCopy == handOrig):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tOriginal hand was {handOrig}")
        print("\tbut implementation of update_hand mutated the original hand!")
        print(f"\tNow the hand looks like this: {handCopy}")
        return
        
    # -----------------------------------
    # Test 2
    # -----------------------------------
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "Evil"

    # Use 'update_hand' function
    hand2 = update_hand(handCopy, word)

    # 'update_hand' can return either one of the following hands
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}

    # Check whether 'update_hand' returns the right answer or not
    if not(hand2 == expected_hand1) and not(hand2 == expected_hand2):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tReturned: {hand2}, \n\t-- but expected: {expected_hand1} or {expected_hand2}")
        return

    # Check that we made a copy of original hand
    if not(handCopy == handOrig):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tOriginal hand was {handOrig}")
        print("\tbut implementation of update_hand mutated the original hand!")
        print(f"\tNow the hand looks like this: {handCopy}")
        return

    # -----------------------------------
    # Test 3
    # -----------------------------------
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    # Use 'update_hand' function
    hand2 = update_hand(handCopy, word)

    # 'update_hand' can return either one of the following hands
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}

    # Check whether 'update_hand' returns the right answer or not
    if not(hand2 == expected_hand1) and not(hand2 == expected_hand2):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tReturned: {hand2}, \n\t-- but expected: {expected_hand1} or {expected_hand2}")
        return

    # Check that we made a copy of original hand
    if not(handCopy == handOrig):
        print(f"FAILURE: test_update_hand({handOrig}, '{word}')")
        print(f"\tOriginal hand was {handOrig}")
        print("\tbut implementation of update_hand mutated the original hand!")
        print(f"\tNow the hand looks like this: {handCopy}")
        return

    # If everything goes well, print SUCCESS!!!
    print("SUCCESS: test_update_hand()")

# -----------------------------------
# test_is_valid_word function
# -----------------------------------
def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    success = True

    # -----------------------------------
    # Test 1
    # -----------------------------------
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    # Use 'is_valid_word' and check result
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected True, but got False for word: '{word}' and hand: {handOrig}")
        success = False

    # Test a second time to see if 'word_list' or 'hand' has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        if handCopy != handOrig:
            print(f"\tTesting word '{word}' for a second time - be sure you're not modifying hand.")
            print(f"\tAt this point, hand ought to be {handOrig}, but it is {handCopy}")

        else:
            print(f"\tTesting word '{word}' for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print(f"The word {word} should be in word_list - is it? {wordInWL}")

        print(f"\tExpected True, but got False for word: '{word}' and hand: {handCopy}")
        success = False

    # -----------------------------------
    # Test 2
    # -----------------------------------
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    # Use 'is_valid_word' and check result
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {handOrig}")
        success = False

    # -----------------------------------
    # Test 3
    # -----------------------------------
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    # Use 'is_valid_word' and check result
    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected True, but got False for word: '{word}' and hand: {handOrig}")
        success = False
    
    # -----------------------------------
    # Test 4
    # -----------------------------------
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    # Use 'is_valid_word' and check result
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {handOrig}")
        success = False

    # -----------------------------------
    # Test 5
    # -----------------------------------
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"
    
    # Use 'is_valid_word' and check result
    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected True, but got False for word: '{word}' and hand: {handOrig}")
        success = False
        
    # -----------------------------------
    # Test 6
    # -----------------------------------
    word = "Even"

    # Use 'is_valid_word' and check result
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {handOrig}")
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        success = False       

    # If everything goes well, print SUCCESS!!!
    if success:
        print("SUCCESS: test_is_valid_word()")

# -----------------------------------
# test_wildcard function
# -----------------------------------
def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    success = True

    # -----------------------------------
    # Test 1
    # -----------------------------------
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    # Use 'is_valid_word' function
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {hand}")
        success = False

    # -----------------------------------
    # Test 2
    # -----------------------------------
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    # Use 'is_valid_word' function
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {hand}")
        success = False

    # -----------------------------------
    # Test 3
    # -----------------------------------
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    # Use 'is_valid_word' function
    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print(f"\tExpected True, but got False for word: '{word}' and hand: {hand}")
        success = False

    # -----------------------------------
    # Test 4
    # -----------------------------------
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    # Use 'is_valid_word' function
    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print(f"\tExpected False, but got True for word: '{word}' and hand: {hand}")
        success = False
    
    # -----------------------------------
    # Test 5
    # -----------------------------------
    # Dictionary of words and scores with wildcards
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    
    # Loop through each key in dictionary
    for (word, n) in words.keys():
        # Use get_word_score function
        score = get_word_score(word, n)

        # Check whether computed score is equal to the actual score of the word or not
        if not(score == words[(word, n)]):
            print("FAILURE: test_get_word_score() with wildcards")
            print(f"\tExpected {words[(word, n)]} points but got {score} for word '{word}', n = {n}")
            success = False

    # If everything goes well, print SUCCESS!!!
    if success:
        print("SUCCESS: test_wildcard()")

# -----------------------------------
# RUN MAIN FUNCTION
# -----------------------------------
if __name__ == '__main__':
    main()

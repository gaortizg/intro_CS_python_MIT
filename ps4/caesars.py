import string
"""
This file implements Caesar's cipher through classes and
routines.
"""

# Define file name as a global variable
WORDLIST_FILENAME = 'words.txt'

# --------------------------
# main function
# --------------------------
def main():
    # -------------------------------------
    # Test case 1 (PlaintextMessage)
    # -------------------------------------
    print("Test case 1:")
    plaintext = PlaintextMessage("hello", 2)
    print("Expected Output: jgnnq")
    print(f"Actual Output: {plaintext.get_message_text_encrypted()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 2 (CiphertextMessage)
    # -------------------------------------
    print("Test case 2:")
    ciphertext = CiphertextMessage("jgnnq")
    print("Expected Output:", (24, 'hello'))
    print(f"Actual Output: {ciphertext.decrypt_message()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 3 (PlaintextMessage)
    # -------------------------------------
    print("Test case 3:")
    plaintext = PlaintextMessage("hello", 10)
    print("Expected Output: rovvy")
    print(f"Actual Output: {plaintext.get_message_text_encrypted()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 4 (CiphertextMessage)
    # -------------------------------------
    print("Test case 4:")
    ciphertext = CiphertextMessage("Rovvy")
    print("Expected Output:", (16, 'Hello'))
    print(f"Actual Output: {ciphertext.decrypt_message()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 5 (PlaintextMessage)
    # -------------------------------------
    print("Test case 5:")
    plaintext = PlaintextMessage("CORNERs", 21)
    print("Expected Output: XJMIZMn")
    print(f"Actual Output: {plaintext.get_message_text_encrypted()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 6 (CiphertextMessage)
    print("Test case 6:")
    # -------------------------------------
    ciphertext = CiphertextMessage("XJMIZMn")
    print("Expected Output:", (5, 'CORNERs'))
    print(f"Actual Output: {ciphertext.decrypt_message()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 7 - Unencrypt story
    # -------------------------------------
    print("Test case 7 (Decipher story):")
    encripted_story = CiphertextMessage(get_story_string())
    best_shift, deciphered_story = encripted_story.decrypt_message()
    print(f"Shift value: {best_shift}")
    print(f"Unencrypted story:\n\n{deciphered_story}")
    print()

# --------------------------
# load_words function
# --------------------------
def load_words(file_name):
    """
    This function loads a list of words from a text file

    Input:
    file_name (string): the name of the file containing the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print(f"{len(wordlist)} words loaded.")
    return wordlist

# --------------------------
# is_word function
# --------------------------
def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring capitalization and punctuation

    Input:
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

# --------------------------
# get_story_string function
# --------------------------
def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

# ---------------------------------------
# Class definition for 'Message' Object
# ---------------------------------------
class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    # ----------------------------------------------------------
    # 'get_message_text' method definition for class 'Message'
    # ----------------------------------------------------------
    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        """
        return self.message_text

    # ----------------------------------------------------------
    # 'get_valid_words' method definition for class 'Message'
    # ----------------------------------------------------------
    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        """
        return self.valid_words.copy()

    # ----------------------------------------------------------
    # 'build_shift_dict' method definition for class 'Message'
    # ----------------------------------------------------------
    def build_shift_dict(self, shift):
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns:
        A dictionary mapping a letter (string) to another letter (string). 
        """
        # Create a string with upper and lowercase letters
        alpha_upper = string.ascii_uppercase
        alpha_lower = string.ascii_lowercase

        # Initialize dictionary to be returned by method
        caesar_dict = {}

        # Loop through each case
        for alphabet in [alpha_upper, alpha_lower]:
            # Loop through each letter
            for letter in alphabet:
                if letter.isupper():
                    char_shift = (ord(letter) - ord('A') + shift) % 26
                    char_shift = chr(char_shift + ord('A'))
                else:
                    char_shift = (ord(letter) - ord('a') + shift) % 26
                    char_shift = chr(char_shift + ord('a'))

                # Add letter to dictionary with its respective value
                caesar_dict[letter] = char_shift
        
        # Return dictionary
        return caesar_dict

    # ----------------------------------------------------------
    # 'apply_shift' method definition for class 'Message'
    # ----------------------------------------------------------
    def apply_shift(self, shift):
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns:
        The message text (string) in which every character is shifted down
        the alphabet by the input shift
        """
        # Get dictionary with mapping of letters defined by 'shift'
        caesar_dict = self.build_shift_dict(shift)

        # Initialize string
        shifted_text = ""

        # Apply Caesars' cipher to text
        for letter in self.message_text:
            # If there is a letter, shift letter by value defined in dictionary
            if letter in caesar_dict:
                shifted_text += caesar_dict[letter]

            # Preserve white spaces, special characters, and numbers
            else:
                shifted_text += letter

        # Return text with shifted words
        return shifted_text

    # ----------------------------------------------------------
    # '__str__' method definition for class 'Message'
    # ----------------------------------------------------------
    def __str__(self):
        # This method tells Python how to print output 
        # of this object using function 'print'
        return str(self.message_text)

# ------------------------------------------------
# Class definition for 'PlaintextMessage' Object
# ------------------------------------------------
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        # Inherit attributes from object 'Message'
        Message.__init__(self, text)

        # Initialize other attributes not in 'Message' object
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    # ----------------------------------------------------------
    # 'get_shift' method definition for class 'PlaintextMessage'
    # ----------------------------------------------------------
    def get_shift(self):
        """
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        """
        return self.shift

    # ----------------------------------------------------------
    # 'get_encryption_key' method definition for class 'PlaintextMessage'
    # ----------------------------------------------------------
    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        """
        return self.encryption_dict.copy()

    # ----------------------------------------------------------
    # 'get_message_text_encrypted' method definition for class 'PlaintextMessage'
    # ----------------------------------------------------------
    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    # ----------------------------------------------------------
    # 'change_shift' method definition for class 'PlaintextMessage'
    # ----------------------------------------------------------
    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.     
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        """
        # Validate shift value with 'assert'
        assert (0 <= shift) and (shift < 26), "Invalid shift amount!"

        # Updates attributes of 'PlaintextMessage' object
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

# ------------------------------------------------
# Class definition for 'CiphertextMessage' Object
# ------------------------------------------------
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Inherit attributes from object 'Message'. Notice that the two attributes
        # of the 'CiphertextMessage' object match the two attributes of the 
        # 'Message' object
        Message.__init__(self, text)

    # ----------------------------------------------------------
    # 'decrypt_message' method definition for class 'CiphertextMessage'
    # ----------------------------------------------------------
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Initialize list where to store results
        cipher_scan = []

        # Loop through each letter in the alphabet
        for shift_value in range(26):
            # Decipher message using current shift_value
            decipher_text = self.apply_shift(shift_value)

            # Check each word in 'decipher_text' and check whether
            # is a word or not. Increase counter for each valid word
            valid_words = 0
            for word in decipher_text.split():
                if is_word(self.valid_words, word):
                    valid_words += 1
                
                # Store results in list as a tuple
                # (valid_words, shift_value, decipher_text)
                cipher_scan.append((valid_words, shift_value, decipher_text))
            
        # Obtain tuple with max number of 'valid_words'
        best_result = max(cipher_scan, key = lambda i : i[0])

        # Return best result (shift_value, decipher_text)
        return best_result[1:]

# --------------------------
# RUN MAIN FUNCTION
# --------------------------
if __name__ == '__main__':
    main()
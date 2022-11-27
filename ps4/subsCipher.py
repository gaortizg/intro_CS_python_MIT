import string
from permutations import get_permutations
"""
This file implements a substitution cipher through classes and
routines.
"""

# Define useful global variables
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
WORDLIST_FILENAME = 'words.txt'

# --------------------------
# main function
# --------------------------
def main():
    # -------------------------------------
    # Test case 1 (SubMessage)
    # -------------------------------------
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print(f"Original message: {message.get_message_text()} Permutation: {permutation}")
    print("Expected encryption: Hallu Wurld!")
    print(f"Actual encryption: {message.apply_transpose(enc_dict)}")
    print("-" * 10)
    
    # -------------------------------------
    # Test case 1 (EnryptedSubMessage)
    # -------------------------------------
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print(f"Decrypted message: {enc_message.decrypt_message()}")
    print("-" * 10)
     
    # -------------------------------------
    # Test case 2 (SubMessage)
    # -------------------------------------
    message = SubMessage("Testing and TRYING my new CODE!!")
    permutation = "uoeia"
    enc_dict = message.build_transpose_dict(permutation)
    print(f"Original message: {message.get_message_text()} Permutation: {permutation}")
    print("Expected encryption: Tosteng und TRYENG my now CIDO!!")
    print(f"Actual encryption: {message.apply_transpose(enc_dict)}")
    print("-" * 10)
    
    # -------------------------------------
    # Test case 2 (EnryptedSubMessage)
    # -------------------------------------
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print(f"Decrypted message: {enc_message.decrypt_message()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 3 (SubMessage)
    # -------------------------------------
    message = SubMessage("Creating A different test WITH diffeRENT CAseS")
    permutation = "aeiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print(f"Original message: {message.get_message_text()} Permutation: {permutation}")
    print("Expected encryption: Creating A different test WITH diffeRENT CAseS")
    print(f"Actual encryption: {message.apply_transpose(enc_dict)}")
    print("-" * 10)
    
    # -------------------------------------
    # Test case 3 (EnryptedSubMessage)
    # -------------------------------------
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print(f"Decrypted message: {enc_message.decrypt_message()}")
    print("-" * 10)

    # -------------------------------------
    # Test case 4 (SubMessage)
    # -------------------------------------
    message = SubMessage("Time to check and Undo encrYPTION")
    permutation = "eiauo"
    enc_dict = message.build_transpose_dict(permutation)
    print(f"Original message: {message.get_message_text()} Permutation: {permutation}")
    print("Expected encryption: Tami tu chick end Ondu incrYPTAUN")
    print(f"Actual encryption: {message.apply_transpose(enc_dict)}")
    print("-" * 10)
    
    # -------------------------------------
    # Test case 4 (EnryptedSubMessage)
    # -------------------------------------
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print(f"Decrypted message: {enc_message.decrypt_message()}")
    print("-" * 10)

# --------------------------
# 'load_words' function
# --------------------------
def load_words(file_name):
    """
    Input:
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns:
    A list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print(len(wordlist), "words loaded.")
    return wordlist

# --------------------------
# 'is_word' function
# --------------------------
def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring capitalization and punctuation

    Input:
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns:
    True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

# ---------------------------------------
# Class definition for 'SubMessage' Object
# ---------------------------------------
class SubMessage(object):
    def __init__(self, text):
        """
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    # ----------------------------------------------------------
    # 'get_message_text' method definition for class 'SubMessage'
    # ----------------------------------------------------------
    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        """
        return self.message_text

    # ----------------------------------------------------------
    # 'get_valid_words' method definition for class 'SubMessage'
    # ----------------------------------------------------------
    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        """
        return self.valid_words.copy()

    # ----------------------------------------------------------
    # 'build_transpose_dict' method definition for class 'SubMessage'
    # ----------------------------------------------------------     
    def build_transpose_dict(self, vowels_permutation):
        """
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        """
        # Initialize dictionary to be returned by method
        transpose_dict = {}

        # Number of vowels and consonants
        len_vowels = len(VOWELS_LOWER)
        len_consonants = len(CONSONANTS_LOWER)

        # Loop through each vowel
        for i in range(len_vowels):
            transpose_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()
            transpose_dict[VOWELS_LOWER[i]] = vowels_permutation[i].lower()
            
        # Loop through each consonant
        for i in range(len_consonants):
            transpose_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
            transpose_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]

        # Return dictionary
        return transpose_dict
    
    # ----------------------------------------------------------
    # 'apply_transpose' method definition for class 'SubMessage'
    # ----------------------------------------------------------
    def apply_transpose(self, transpose_dict):
        """
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        """
        # Initialize string
        encrypted_text = ""

        # Apply substitution cipher to text
        for letter in self.message_text:
            # If there is a letter, substitute letter by value defined in dictionary
            if letter in transpose_dict:
                encrypted_text += transpose_dict[letter]

            # Preserve white spaces, special characters, and numbers
            else:
                encrypted_text += letter

        # Return encrypted text
        return encrypted_text
    
    # ----------------------------------------------------------
    # '__str__' method definition for class 'SubMessage'
    # ----------------------------------------------------------
    def __str__(self):
        # This method tells Python how to print output 
        # of this object using function 'print'
        return str(self.message_text)

# ---------------------------------------
# Class definition for 'EncryptedSubMessage' Object
# ---------------------------------------
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        """
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        # Inherit attributes from object 'SubMessage'
        SubMessage.__init__(self, text)
    
    # ----------------------------------------------------------
    # 'decrypt_message' method definition for class 'EncryptedSubMessage'
    # ----------------------------------------------------------
    def decrypt_message(self):
        """
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        """
        # Initialize list where to store the results
        decrypt_scan = []

        # Create all possible permutations of vowels
        perm_vowels = get_permutations(VOWELS_LOWER)

        # Loop through each permutation
        for perm in perm_vowels:
            # Create dictionary with the current permutation
            transpose_dict = self.build_transpose_dict(perm)

            # Apply tranpose to encrypted text using current 'transpose_dict'
            decipher_text = self.apply_transpose(transpose_dict)

            # Check each word in 'decipher_text' and check whether
            # is a word or not. Increase counter for each valid word
            valid_words = 0
            for word in decipher_text.split():
                if is_word(self.valid_words, word):
                    valid_words += 1
                
                # Store results in list as a tuple
                # (valid_words, decipher_text)
                decrypt_scan.append((valid_words, decipher_text))
        
        # Obtain tuple with max number of 'valid_words'
        best_result = max(decrypt_scan, key = lambda i : i[0])

        # Return best decrypted message
        return best_result[1]

# --------------------------
# RUN MAIN FUNCTION
# --------------------------
if __name__ == '__main__':
    main()
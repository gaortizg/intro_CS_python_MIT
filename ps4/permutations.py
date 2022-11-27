# --------------------------
# main function
# --------------------------
def main():
    # Example 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:  ', get_permutations(example_input))
    
    # Example 2
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    print('Actual Output:  ', get_permutations(example_input))

    # Example 3
    example_input = 'ale'
    print('Input:', example_input)
    print('Expected Output:', ['ael', 'ale', 'eal', 'ela', 'lae', 'lea'])
    print('Actual Output:  ', get_permutations(example_input))

    # Example 4
    example_input = '1234'
    print('Input:', example_input)
    print('Expected Output:', ['1234', '1243', '1324', '1342', '1423', '1432',
                               '2134', '2143', '2314', '2341', '2413', '2431',
                               '3124', '3142', '3214', '3241', '3412', '3421',
                               '4123', '4132', '4213', '4231', '4312', '4321'])
    print('Actual Output:  ', get_permutations(example_input))

# --------------------------
# get_permutations function
# --------------------------
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    Input:
    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    # Compute length of 'sequence'
    len_seq = len(sequence)

    # Define base case (sequence is a single character)
    if len_seq == 1:
        return sequence
    
    # If sequence is more than one character long
    else:
        # Initialize list to store all possible permutations of 'sequence'
        seq_perm = []

        # Extract first character of sequence
        first_char = sequence[0]

        # Run 'get_permutations' function recursively on 'sequence'
        # without the first character
        perm_set = get_permutations(sequence[1:])

        # Compute length of each permutation in 'perm_set'
        # All elements have the same length
        len_each_perm = len(perm_set[0])

        # Insert first character into each permutation
        for word in perm_set:
            # Add 'first_char' before first character in permutation
            seq_perm.append(first_char + word)

            # Loop through each letter in 'word'
            for i in range(len_each_perm):
                # Case when permutation is one single character
                if len_each_perm == 1:
                    seq_perm.append(word + first_char)
                
                # Because of indexing, I need to add 'first_char' after first
                # letter in permutation 'manually' (using if statement)
                elif i == 0:
                    seq_perm.append(word[0] + first_char + word[1:])
                
                # Add 'first_char' to permutation after each letter
                else:
                    seq_perm.append(word[0:i+1] + first_char + word[i+1:])

    # Order permutations alphabetically and return all possible permutations
    return sorted(seq_perm)

# --------------------------
# RUN MAIN FUNCTION
# --------------------------
if __name__ == '__main__':
    main()
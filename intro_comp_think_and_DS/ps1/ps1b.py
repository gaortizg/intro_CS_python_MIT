def main():
    # --------------------------------
    # Test case 1:
    # --------------------------------
    
    # Define available egg weights (as a tuple)
    egg_weights1 = (1, 5, 10, 25)

    # Amount of weight we want to find eggs to fit
    n1 = 99

    # Find smallest number of eggs needed to make target weight
    n_eggs1 = dp_make_weight(egg_weights1, n1, {})
    # Print info on screen
    print(f"Egg weights = {egg_weights1}")
    print(f"n = {n1}")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print(f"Actual output: {n_eggs1}")
    print("--------------------------------------------------")

    # --------------------------------
    # Test case 2:
    # --------------------------------
    
    # Define available egg weights (as a tuple)
    egg_weights2 = (1, 5, 10, 20)

    # Amount of weight we want to find eggs to fit
    n2 = 99

    # Find smallest number of eggs needed to make target weight
    n_eggs2 = dp_make_weight(egg_weights2, n2, {})
    # Print info on screen
    print(f"Egg weights = {egg_weights2}")
    print(f"n = {n2}")
    print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    print(f"Actual output: {n_eggs2}")
    print("--------------------------------------------------")

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # Initialize variabe to count number of eggs. The objective is to minimize
    # the number of eggs. Initial guess = "target_weight" # of eggs
    # (i.e., only eggs with weight = 1)
    min_eggs = target_weight

    # Default case (recursion)
    if target_weight == 1:
        return 1
    
    # For problems already solved, use "Dynamic Programming"
    # i.e., retrieve result from "memo"
    try:
        return memo[target_weight]
    except KeyError:
        # Loop through each weight that meets the weight constraint
        for i in [c for c in egg_weights if c <= target_weight]:
            # Explore left branch
            num_eggs = 1 + dp_make_weight(egg_weights, target_weight - i, memo)
            
            # Choose best solution (i.e., lowest number of eggs). Update memo
            if num_eggs < min_eggs:
                min_eggs = num_eggs
                memo[target_weight] = min_eggs
    
    # Return best solution (min. number of eggs)
    return min_eggs


# Run 'main' function
if __name__ == "__main__":
    main()
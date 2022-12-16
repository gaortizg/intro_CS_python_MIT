from ps1_partition import get_partitions
import time

def main():
    # Compare greedy vs. brute force optimization
    compare_cow_transport_algorithms()


#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contains data in the
    form of comma-separated < cow name, weight > pairs, and return a dictionary
    containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # Initialize dictionary
    cows_dict = {}

    # Open file and read contents
    with open(filename, "r") as file:
        for line in file:
            name, weight = line.strip().split(",")
            cows_dict[name] = int(weight)

    # Return dictionary
    return cows_dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int - Default = 10)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Make copy of dictionary (to avoid any side-effects). Sort items
    # based on 'weight' from largest to smallest.
    # Result is a list of tuples: (cow name, weight)
    cows_copy = sorted(cows.items(), key=lambda x:x[1], reverse=True)

    # Convert sorted list back to dictionary
    cows_copy = dict(cows_copy)

    # Initialize list where to store all the trips
    trips = []

    # Compute trips
    while len(cows_copy) > 0:
        # Initialize variables for each trip
        trip = []
        total_weight = 0

        # Loop through each cow in dictionary
        for key in cows_copy:
            if (total_weight + cows_copy[key]) <= limit:
                trip.append(key)
                total_weight += cows_copy[key]
        
        # Delete cows that are in current trip
        for name in trip:
            del cows_copy[name]
        
        # Append current trip to list of all trips
        trips.append(trip)

    # Return list containing all the trips
    return trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips.
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int - Default = 10)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Make copy of dictionary (to avoid any side-effects). No need to sort
    cows_copy = cows.copy()

    # Initialize variabe to count number of trips. The objective is to minimize
    # the number of trips. Initial guess could be any large number. I assumed the
    # worst case = one cow per trip
    n_trips = len(cows_copy)

    # Loop through all the possible combinations of trips
    for partition in get_partitions(cows_copy):
        # Auxiliary boolean to check a trip has honored the weight constraint
        valid_trip = True

        # Compute total weight of each trip in partition. If any of the trips
        # has a total weight > limit, then this partition cannot be a solution
        # to optimization problem
        for trip in partition:
            # Initialize variable
            total_weight = 0

            # Loop through each cow in each trip. Add weights
            for cow in trip:
                total_weight += cows_copy[cow]

            # Check if constraint is being honored
            if total_weight > limit:
                valid_trip = False
                break
        
        # If the trip does not break constraint
        if valid_trip:
            # We need to save the solution with the least amount of trips
            # that does not violate the weight constraint
            if len(partition) < n_trips:
                n_trips = len(partition)
                trips = partition

    # Return list containing all the trips with least amount of trips
    return trips


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # Load file
    cows = load_cows("ps1_cow_data.txt")

    # Run greedy optimization algorithm (default Limit=10)
    start = time.time()
    trips_greedy = greedy_cow_transport(cows)
    end = time.time()

    # Print results greedy algorithm
    print(f"Number of trips returned by Greedy algorithm: {len(trips_greedy)}")
    print("Trips returned by Greedy algorithm:")
    for i in range(len(trips_greedy)):
        print(f"Trip {i+1}: {trips_greedy[i]}")
    print(f"How long Greedy algorithm took: {end - start} s.")
    print("--------------------------------------------------")

    # Run brute force optimization algorithm (default Limit=10)
    start = time.time()
    trips_brute = brute_force_cow_transport(cows)
    end = time.time()

    # Print results brute force algorithm
    print(f"Number of trips returned by Brute Force algorithm: {len(trips_brute)}")
    print("Trips returned by Brute Force algorithm:")
    for i in range(len(trips_brute)):
        print(f"Trip {i+1}: {trips_brute[i]}")
    print(f"How long Brute Force algorithm took: {end - start} s.")
    print("--------------------------------------------------")


# Run 'main' function
if __name__ == "__main__":
    main()
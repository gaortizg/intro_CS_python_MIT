def main():
    # Create list of food items
    names = ["wine", "beer", "pizza", "burguer",
             "fries", "coke", "apple", "donut"]

    # Create list of value for each food item
    values = [89, 90, 95, 100, 90, 79, 50, 10]

    # Create list with calories for each food item
    calories = [123, 154, 258, 354, 365, 150, 95, 195]

    # Create menu
    foods = buildMenu(names, values, calories)

    # Rn unit tests
    testGreedys(foods, 750)


# Define class Food
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ": <" + str(self.value)\
                         + ", "  + str(self.calories) + ">"
    

# Function to create menu with 'Food' items
def buildMenu(names, values, calories):
    """
    names, values, calories -> Lists of same length
    names -> List of strings
    values, calories -> Lists of numbers

    Return: List of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    
    return menu


# Function of a Greedy algorithm (Flexible greedy)
def greedy(items, maxCost, keyFn):
    """
    items -> List of Food objects
    maxCost >= 0
    keyFn -> maps elements of items to numbers

    Return:
    - List with items selected by greedy algorithm
    - Total cost of selected items
    """
    # Make copy of items (to avoid any side-effects). Sort items
    # based on 'keyFn' from best to worst. Best and worst defined
    # by 'keyFn'
    itemsCopy = sorted(items, key=keyFn, reverse=True)

    # Initialize variables
    result = []
    totalValue, totalCost = 0.0, 0.0

    # Loop through each item in sorted list
    for i in range(len(itemsCopy)):
        # Keep accumulating items if constraint honored
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    
    return (result, totalValue)


# Funtion to test greedy algorithm
def testGreedy(items, constraint, keyFn):
    # Run greedy algorithm
    taken, val = greedy(items, constraint, keyFn)

    # print results
    print (f"Total value of items taken = {val}")
    for item in taken:
        print(" ", item)


# Define unit tests
def testGreedys(foods, maxUnits):
    # Case 1: Greedy algorithm by Food value
    print(f"Use greedy by value to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.getValue)

    # Case 2: Greedy algorithm by Food cost (cheapest)
    print(f"Use greedy by cost to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

    # Case 3: Greedy algorithm by Food density (see Food class def.)
    print(f"Use greedy by density to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.density)


# Run 'main' function
if __name__ == "__main__":
    main()
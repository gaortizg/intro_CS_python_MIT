import numpy as np
'''
Program to determine the right amount to save away in order to afford 
a down payment on a house in 36 months (assuming semi-annual rise on salary)
'''

# Define known data as global variables
TOTAL_COST = 1000000            # Total cost of house
PORTION_DOWN_PAYMENT = 0.25     # Portion of cost needed for a down payment
ANNUAL_R = 0.04                 # Annual return 'r'
SEMI_ANNUAL_RAISE = 0.07        # Semi-annual raise in salary
MONTHS = 36                     # Number of months to make down payment

def main():
    # Ask for starting annual salary and validate input data
    start_annual_salary = input("Enter the starting salary: ")
    while True:
        try:
            start_annual_salary = int(start_annual_salary)
            if start_annual_salary <= 0:
                start_annual_salary = input("Enter the starting salary: ")
            else:
                break
        except ValueError:
            start_annual_salary = input("Enter the starting salary: ")

    # Amount to save
    amount_to_save = PORTION_DOWN_PAYMENT * TOTAL_COST

    # Define low, high of savings rate range
    low = 0
    high = 1

    # Perform bisection search recursively 
    optimal_rate = bisection_search(low, high, start_annual_salary, amount_to_save)

    # Print results (up to 4 decimal places in case of valid output)
    if optimal_rate == 0:
        print(f"It is not possible to pay the down payment in {MONTHS} months.")
    else:
        print(f"Best savings rate: {optimal_rate:,.4f}")

# Define bisection search as a function to be used recursively
def bisection_search(low, high, start_annual_salary, amount_to_save):
    # Initial guess of optimal savings rate
    savings_rate = (high + low) / 2

    # Compute right amount to save away so as to make down payment in
    # specific number of months
    while True:
        # Restart variables
        current_savings = 0
        annual_salary = start_annual_salary
        monthly_salary = annual_salary/12
        
        # Compute monthly contribution with assumed savings rate
        monthly_contribution = savings_rate * monthly_salary

        # Compute amount saved in specified months with assumed savings rate
        for month in range(MONTHS):
            # Check for semi-annual rise. Update salary and monthly contribution accordingly
            if ((month % 6) == 0) and (month > 0):
                annual_salary *= (1 + SEMI_ANNUAL_RAISE)
                monthly_salary = annual_salary / 12
                monthly_contribution = savings_rate * monthly_salary
        
            # Increase savings monthly contribution + ROI
            current_savings += monthly_contribution + current_savings * ANNUAL_R /12
        
        # Default cases (to stop recursion)
        if  np.abs(low - high) < 0.0001:
            return 0
        elif (np.abs(amount_to_save - current_savings) < 100):
            return savings_rate

        # Apply bisection method recursively
        if current_savings < amount_to_save:
            return bisection_search(savings_rate, high, start_annual_salary, amount_to_save)
        else:
            return bisection_search(low, savings_rate, start_annual_salary, amount_to_save)

# Run main function
main()
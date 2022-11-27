'''
Program to determine how long it will take to save enough money
to make the down payment on a house
'''

# Define known data as global variables
PORTION_DOWN_PAYMENT = 0.25     # Portion of cost needed for a down payment
ANNUAL_R = 0.04                 # Annual return 'r'

def main():
    # Ask for annual salary and validate input data
    annual_salary = input("Enter your annual salary: ")
    while True:
        try:
            annual_salary = int(annual_salary)
            if annual_salary <= 0:
                annual_salary = input("Enter your annual salary: ")
            else:
                break
        except ValueError:
            annual_salary = input("Enter your annual salary: ")

    # Ask for percentage of salary to save and validate input data
    portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
    while True:
        try:
            portion_saved = float(portion_saved)
            if (portion_saved <= 0) or (portion_saved > 1):
                portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
            else:
                break
        except ValueError:
            portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
    
    # Ask for total cost of house to buy and validate input data
    total_cost = input("Enter the cost of your dream home: ")
    while True:
        try:
            total_cost = int(total_cost)
            if total_cost <= 0:
                total_cost = input("Enter the cost of your dream home: ")
            else:
                break
        except ValueError:
            total_cost = input("Enter the cost of your dream home: ")

    # Initialize variables
    current_savings = 0
    months = 0

    # Compute monthly salary and monthly contribution
    monthly_salary = annual_salary / 12
    monthly_contribution = portion_saved * monthly_salary

    # Amount to save
    amount_to_save = PORTION_DOWN_PAYMENT * total_cost

    # Compute number of months needed to make down payment
    while current_savings < amount_to_save:
        # Increase savings by ROI and percentage of monthly salary
        current_savings += monthly_contribution + current_savings * ANNUAL_R / 12

        # Increase number of months
        months += 1

    # Print result
    print(f"Number of months: {months}")

# Run main function
main()
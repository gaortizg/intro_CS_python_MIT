import numpy as np

# PS0 from the course
def main():
    # Validate inputs
    x = input("Enter number x: ")
    while True:
        try:
            x = int(x)
            break
        except ValueError:
            x = input("Enter number x: ")
    
    y = input("Enter number y: ")
    while True:
        try:
            y = int(y)
            break
        except ValueError:
            y = input("Enter number y: ")

    # Compute requested results:
    ans1 = int(x) ** int(y)
    ans2 = np.log2(x)

    # print results on screen
    print(f"x**y = {ans1}")
    print(f"log2(x) = {ans2}")

# Run main function
main()
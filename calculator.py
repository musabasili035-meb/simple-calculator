# Display the title of the program
print("---SIMPLE CALCULATOR---")

# Ask the user to enter the first number
# The input is converted from string to float to allow decimal calculations
x = float(input("Enter first number: "))

# Ask the user to enter the second number
# This value will be used in all arithmetic operations
y = float(input("Enter second number: "))

# Display the list of available arithmetic operations
print("\nChoose operation:")
print("+  Addition")        # Option for addition
print("-  Subtraction")     # Option for subtraction
print("*  Multiplication")  # Option for multiplication
print("/  Division")        # Option for division

# Ask the user to choose an operator from the displayed options
operator = input("\nEnter operator: ")

# Check if the selected operator is addition
if operator == "+":
    # Add the two numbers and display the result
    print("Summation is:", x + y)

# Check if the selected operator is subtraction
elif operator == "-":
    # Subtract the second number from the first and display the result
    print("Difference is:", x - y)

# Check if the selected operator is multiplication
elif operator == "*":
    # Multiply the two numbers and display the result
    print("Product is:", x * y)

# Check if the selected operator is division
elif operator == "/":
    # Check if the second number is zero to avoid division by zero error
    if y == 0:
        # Display error message if division by zero is attempted
        print("Error: Division by zero is not allowed")
    else:
        # Perform division and display the result
        print("Division is:", x / y)

# Execute this block if the entered operator is not valid
else:
    # Display error message for invalid operator input
    print("Invalid operator selected")

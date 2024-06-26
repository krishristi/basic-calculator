# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Main function to run the calculator
def calculator():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

# Run the calculator
calculator()

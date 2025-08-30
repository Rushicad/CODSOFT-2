def get_number(prompt):
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

def main():
    print("Simple Calculator")
    print("-----------------")
    
    # Get two valid numbers from the user
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    # Operation menu
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get valid operation choice
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break
        print("Invalid choice! Please select 1-4.")
    
    # Perform calculation
    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        try:
            result = num1 / num2
            operation = "/"
        except ZeroDivisionError:
            print("\nError: Division by zero is not allowed!")
            return
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
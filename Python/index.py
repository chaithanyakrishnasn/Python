def greet(name):
    """
    A simple function to greet a person by name.
    """
    return f"Hello, {name}! Welcome to Python programming."

def calculate_square(number):
    """
    Calculate the square of a given number.
    """
    return number ** 2

def main():
    # Get user input
    user_name = input("Please enter your name: ")
    
    # Greet the user
    greeting = greet(user_name)
    print(greeting)
    
    # Calculate and display the square of a number
    try:
        number = float(input("Enter a number to calculate its square: "))
        result = calculate_square(number)
        print(f"The square of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
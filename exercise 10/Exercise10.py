# Function to check whether a number is odd or even
def check_even_odd(number):
    # If the number divides evenly by 2, it's even
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # Otherwise, it's odd
        return f"{number} is odd."

# Main function to get user input and display the result
def main():
    try:
        # Ask the user to enter a number
        user_number = int(input("Please enter a number: "))
        
        # Check if it's even or odd
        result_message = check_even_odd(user_number)
        
        # Print the result
        print(result_message)
    except ValueError:
        # If the user enters something that's not a valid number
        print("Invalid input. Please enter a valid integer.")

# This ensures the main function runs only if the script is executed directly
if __name__ == "__main__":
    main()

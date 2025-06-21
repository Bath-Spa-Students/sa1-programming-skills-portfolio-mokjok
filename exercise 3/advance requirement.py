# ask the user to type their fyll name, remove unnecessary whitespaces.
user_name = input("Enter your full name: ").strip() #.strip() remove unnecessary whitespaces surrounding input

# ask the user hometown and remove unnecessary whitespaces.
user_hometown = input("Enter your hometown: ").strip() #.strip() remove unnecessary whitespaces surrounding input

# for not making a mistake, again ask the user for their age.
while True:
    try:
        # Make an integer out of the input.
        user_age = int(input("Enter your age: "))
        break  # If the conversion is successful, do not ask their age again.
    except ValueError:
        # If the input is not a valid integer, display an error.
        print("Invalid input. Please enter a numerical value for age.")

# Print the collected information.
print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")
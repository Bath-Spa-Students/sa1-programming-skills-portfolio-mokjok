# This dictionary has countries and their capitals
quiz_data = {
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Greece": "Athens",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Spain": "Madrid",
    "France": "Paris",
    "Italy": "Rome",
    "Germany": "Berlin"
}

# This keeps track of how many correct answers the user gives
score = 0

# Go through each country in the dictionary
for country, capital in quiz_data.items():
    # Ask the user to write the capital of the country
    user_answer = input(f"What's the capital of {country}? ").strip()  # removes extra spaces if any

    # Check if the answer is right (ignoring small/big letters)
    if user_answer.lower() == capital.lower():
        # Right answer, so give a message and add 1 to score
        print("Good. That's correct.")
        score += 1
    else:
        # Wrong answer, so tell the correct capital
        print(f"Close, but the capital of {country} is actually {capital}.")

# Show the total correct answers at the end
print(f"\nGreat job. You scored {score} out of {len(quiz_data)}.")

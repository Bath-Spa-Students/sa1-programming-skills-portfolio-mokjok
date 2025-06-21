#create a correct password for the system.
Correct_password = "12345"

#how many password attempts are allowed.
Max_attempts = 5

#create a counter to record the number of attempts made.
Attempts = 0

#ask the user to write the right password again and again until they enter the right password or the tries have finished.
while Attempts < Max_attempts:
    #request the user to enter their password.
    User_password = input("Enter the password: ").strip()
    
    #due to privacy purposes hide the entered password with asterisks.
    masked_password = '*' * len(User_password)
    
    #After every attempt, increase the number of attempts by one.
    Attempts += 1

    #check that the password user typed and the one user have stored are the same.
    if User_password == Correct_password:
        #If it's correct, allow access and close the loop.
        print("Access is granted. Greetings, User.")
        break
    else:
        #If it's wrong, show the masked password and an error message.
        print(f"Access denied: {masked_password}")
        
        #If it is the user second last try, give them a clue.
        if Attempts == Max_attempts - 1:
            print("Hint: The password is birthday.")
        
        #Lock the user out and let them know if they've tried everything.
        if Attempts == Max_attempts:
            print("No access. Because of too many unsuccessful attempts, you have been locked out.")

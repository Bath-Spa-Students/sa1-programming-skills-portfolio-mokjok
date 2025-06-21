#A data structure matches the daily count of non-leap year periods to sequencely month values ranging 1 to 12
days_in_month = {
    1: 31,   # january, 31 days
    2: 28,   # february, 28 days (in a non-leap year)
    3: 31,   # march, 31 days
    4: 30,   # april, 30 days
    5: 31,   # may, 31 days
    6: 30,   # june, 30 days
    7: 31,   # july, 31 days
    8: 31,   # august, 31 days
    9: 30,   # september, 30 days
    10: 31,  # october, 31 days
    11: 30,  # november, 30 days
    12: 31   # december, 31 days
}

#ask a number of month from 1 to 12 from the user.
try:
    month_number = int(input("Enter the month number (1-12): ").strip())  #remove the extra space around the input

    #check number of month you entered falls between 1 and 12.
    if 1 <= month_number <= 12:
        
        #A special example where we must verify for a leap year is February (second month).
        if month_number == 2:
            #ask the user if it's a leap year.
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            #February will have 28 days if it is not a leap year and 29 if it is a leap year.
            days = 29 if is_leap == "yes" else 28
        else:
            #And for other month, check the data structure  for the amount of days.
            days = days_in_month[month_number]
        
        #show how many days there are in the chosen month.
        print(f"The number of days in month {month_number} is {days}.")
    else:
        #if the number of month is not between 1 and 12, display this message.
        print("incorret, That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    #if the user enters a text instead of a number display this message.
    print("I apologize, but that input is invalid. Kindly input a number from 1 to 12.")
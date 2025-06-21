#a list to keep track of the each month's days
#Month numbers are represented by numbers, 1 is for January, 2 for February, and so on., on the other hand the days of each month are represented by values.
Days_in_month = {
    1: 31,   #January
    2: 28,   #February (assume a non-leap year)
    3: 31,   #March
    4: 30,   #April
    5: 31,   #May
    6: 30,   #June
    7: 31,   #July
    8: 31,   #August
    9: 30,   #September
    10: 31,  #October
    11: 30,  #November
    12: 31   #December
}

#prompt the user to enter the month number.
try:
    Month_number = int(input("Enter a month number (1-12): ").strip())#.strip() remove unnecessary space surrounding input

   #confirm that the month number falls within the correct range.
    if Month_number in Days_in_month:
        #Show the number of days in the month that was entered.
        print(f"Number of days in month {Month_number} is {Days_in_month[Month_number]}.")
    else:
        #tell the user if the input is not between 1 and 12.
        print("Sorry, That's not a valid month number. Please enter a number between 1 and 12")

except ValueError:
    #display this message to deal with non-integer input.
    print("Invalid number. Enter a numerical value between 1 and 12")

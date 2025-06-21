#Create a list of strings which contains names
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#In the string list you made, write the string you wish to search for.
Search_name = input("Enter name:").strip()

#show to screen if the name is show up in the search
found = False

#check if the name user have input is similar with the  name available on the list by looping over them.
for name in Names:
    # change both of the names to lowercase,for being sure the search is case insensitive.

    if name.lower() == Search_name.lower():
        #Set 'found' to True and tell the user if a right match is found.
        found = True
        print(f"FOUND'{Search_name}' is present in the list.")

        break  #when user found the name, end the loop.
#tell the user if the loop ends and the name was not found.

if not found:
    print(f"sadly, '{Search_name}' is not in the list.")

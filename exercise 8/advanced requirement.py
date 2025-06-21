# A ready-made names of list to look up
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# ask the user for the user they want to look up to and remove useless spaces.
search_term = input("Kindly type the name you're trying to find: ").strip()

# Use a case-insensitive search to see if the entered name is present in the list.
if search_term.lower() in [name.lower() for name in names]:
    # Send a kind success message if the name is located.
    print(f"Great news. '{search_term}' is in the list.")
else:
    # tell the user if the name is not in the list.
    print(f"Sorry, '{search_term}' isn't in the list.")
# tell the variables for the personal information 
name = "Murtaza"  # the name as a string
hometown = "Pakistan"    # hometown as a string form
age = 18                 # age as an integer

# collect information in a dictionary with descriptive keys
info = {
    "name": name,        # Key "name" with the value of name
    "hometown": hometown, # Key "hometown" with the value of hometown
    "age": age            # Key "age" with the value of age
}

# Print a new line for each piece of the information
print(f"{info['name']}\n{info['hometown']}\n{info['age']}")
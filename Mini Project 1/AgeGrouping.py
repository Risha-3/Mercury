# Empty lists for different age groups are created below.
children = []
teenagers = []
young_adults = []
adults = []

# Ask the user for the number of players.
num_players = int(input("Enter the number of players: "))


for _ in range(num_players):
    while True:  # Loops until valid input.
        name = input("Enter the player's name: ").strip()  # Removes whitespace before and after string.
        if name:  # If the name variable is not empty, break loop and continue with the program (line 19).
            break
        else:
            print("The name field cannot be empty.")

    while True:
        try:
            age = int(input("Enter the player's age: "))
            if age < 0:
                print("Age must be greater than zero, please try again.")
            else:
                break  # Exit loop if input is valid.
        except ValueError:
            print("Age must be a number, please try again.")

    if age < 13:
        children.append(name)  # If age is less than 13, add to children.
    elif 13 <= age <= 19:
        teenagers.append(name)  # If age is between 13 and 19, add to teenagers.
    elif 20 <= age <= 29:
        young_adults.append(name)  # If age is between 20 and 29, add to young_adults.
    else:
        adults.append(name)  # If age is 30 or above, add to adults.

# Print out the age groups.
print("\n")
print("Children:", children)
print("Teenagers:", teenagers)
print("Young Adults:", young_adults)
print("Adults:", adults)

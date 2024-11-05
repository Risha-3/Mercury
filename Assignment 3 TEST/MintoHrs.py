def min_to_hrs(user_minutes):
    """
    This function converts a given number of minutes into hours and minutes.
    It then returns a tuple containing two elements which is the number of hours and the remaining minutes. 
    """
    hours = int(user_minutes // 60)
    minutes = user_minutes % 60
    return hours, minutes
    
print("This program will convert minutes to hours")
print("Type STOP to exit the program")
while True:
    user_input = input("\nEnter the time in minutes (such as 155.5) or STOP: ")
    if user_input.upper() == 'STOP':  # If user types STOP, the loop will break.
        print("You have successfully exit the program. Thank you.")
        break

    try:
        user_minutes = float(user_input) # Converts the minute value typed in by the user into a float.
        hours,minutes = min_to_hrs(user_minutes)  # The variable is passed through the min_to_hrs function.
        print(f"{user_minutes} minutes is equivalent to {hours} hours and {minutes:.2f} minutes.")
    except ValueError:
        print("Invalid input. Please try again.")


# Strings,Integers and Floats
# Inputs and outputs
# Definitions
# Conditionals
# While loop
# Error handling
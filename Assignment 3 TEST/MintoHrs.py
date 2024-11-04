def min_to_hrs(user_minutes):
    hours = int(user_minutes // 60)
    minutes = user_minutes % 60
    return hours, minutes
    
print("This program will convert minutes to hours")
print("Type STOP to exit the program")
while True:
    user_input = input("\nEnter the time in minutes (such as 155.5) or STOP: ")
    if user_input.upper() == 'STOP':
        print("You have successfully exit the program. Thank you.")
        break

    try:
        user_minutes = float(user_input)
        hours,minutes = min_to_hrs(user_minutes)
        print(f"{user_minutes} minutes is equivalent to {hours} hours and {minutes:.2f} minutes.")
    except ValueError:
        print("Invalid input. Please try again.")
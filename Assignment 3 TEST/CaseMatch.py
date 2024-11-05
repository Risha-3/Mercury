def fix_robot():
    """
    This function provides a brief guide on basic maintenance tasks depending on what type of robot you own.
    It prompts the user to select the type of robot that requires maintenance and then outputs the corresponding instructions.
    """
    # Prints title and options to user.
    print("***A very short guide on how to fix a robot***")
    print("""
          What type of robot do you have:
          1. Industrial Robot
          2. Vacuum Robot
          3. Humanoid Robot
          """)
    try:
        robot_type = int(input("Choose your robot type (1, 2, or 3): "))  # Asking the user what option number they want to select.
        match robot_type:
            case 1:
                print("Maintenance: Perform updates, Inspect wiring, Lubricate moving components.")
            case 2:
                print("Empty rubbish, Hard reset, check for any updates.")
            case 3:
                print("Clean sensors, Charge batteries, Check for firmare updates, Perform software updates.")
            case _:  # Default case for invalid input (if the user enters an integer other than 1, 2 or 3).
                print("Invalid selection. Please try again.")
    
    except ValueError:
    # If the user inputs anything other than a valid integer, rather than the program displaying red text, it will raise a ValueError.
    # By doing this, I will be able to inform the user that the input was invalid without crashing the program.
        print("Invalid input! Please enter a number (1, 2, or 3).")


fix_robot()  # Calling the fix_robot function.


# Strings and Intgers
# Inputs and Outputs
# Definitions
# Match-Case Statements
# Error Handling

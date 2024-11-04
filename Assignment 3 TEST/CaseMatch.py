def fix_robot():
    print("***A very short guide on how to fix a robot***")
    print("""
          What type of robot do you have:
          1. Industrial Robot
          2. Vacuum Robot
          3. Humanoid Robot
          """)
    try:
        robot_type = int(input("Choose your robot type (1, 2, or 3): "))
        match robot_type:
            case 1:
                print("Maintenance: Perform updates, Inspect wiring, Lubricate moving components.")
            case 2:
                print("Empty rubbish, Hard reset, check for any updates.")
            case 3:
                print("Clean sensors, Charge batteries, Check for firmare updates, Perform software updates.")
            case _:
                print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")


fix_robot()
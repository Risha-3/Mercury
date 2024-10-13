inventory = []

print("\n****** The Rogue Unit ******")
print("\nIn the distant future, Earth has been abandoned by humans and is now inhabited solely by robots."
      "\nFor centuries, the robots have been self-sustaining, but recently their power source has started to fail. Without it, all the robots will eventually shut down."
      "\nYou play as Unit T45, a maintenance robot with a malfunctioning memory unit, making you curious and self-aware — traits that set you apart from other robots."
      "\nYou have received a mysterious signal hinting at an ancient backup power source"
      "\nYour mission is to navigate the dangerous, abandoned city, locate the backup power source, and restore life to your fellow machines before the power source runs out of energy. However, there are several challenges ahead: rogue robots, environmental hazards, and your own damaged memory, which makes you question who to trust."
      "\n")

print("You are in a factory. Do you want to:")
print("1. Head towards the City of Machines")
print("2. Explore the Wastelands for spare parts")
print("3. Investigate the signal origin nearby")
choice1 = int(input("What do you want to do? (Enter 1, 2 or 3) "))

if (choice1 == 1):
    print("\nYou move towards the City of Machines, navigating through broken roads and abandoned structures.")
    print("As you get closer, you encounter a group of rogue robots!")

    print("\nDo you want to")
    print("1. Fight the rogue robots")
    print("2. Try and sneak past them")
    choice2 = int(input("What do you want to do? (Enter 1 or 2): "))

    if (choice2 == 1):
        print("\nYou charge into battle! Using your maintenance tools, you manage to disable the rogue robots.")
        print("You continue your journey towards the City of Machines.")
    elif (choice2 == 2):
        print("\nYou manage to sneak past the rogue robots without being detected.")
        print("You continue your journey safely.")
    else:
        print("\nInvalid choice. The rogue robots spot you, and you must run for your life!")

elif (choice1 == 2):
    print("\nYou explore the Wastelands, searching through piles of scrap metal for spare parts.")
    print("You find a broken-down military robot named V-RX9 who offers to help you if you repair him.")
    
    print("\nDo you want to:")
    print("1. Repair V-RX9")
    print("2. Salvage parts from V-RX9")
    choice3 = int(input("What do you want to do? (Enter 1 or 2): "))

    if (choice3 == 1):
        print("\nYou repair V-RX9! He decides to join you on your journey to the City of Machines.")
    elif (choice3 == 2):
        print("\nYou decide to dismantle V-RX9 and find weapons and body armour.")
        inventory.append("M16 rifle")
        inventory.append("Ballistic Vest")
        print("\nYou have", inventory, "in your inventory.")
    else:
        print("\nInvalid choice. You waste too much time deciding, and night falls. You must find shelter.")

elif (choice1 == 3):
    print("\nYou move towards the origin of the mysterious signal.")
    print("Suddenly, a trap activates! You barely avoid a falling structure.")
    
    print("\nDo you:")
    print("1. Investigate the area for clues")
    print("2. Leave the area and head to the City of Machines")
    choice4 = int(input("What do you want to do? (Enter 1 or 2): "))

    if (choice4 == 1):
        print("\nYou find an old data chip and a dormant trap hidden in the debris. The chip may contain valuable information about the signal.")
        inventory.append("Data chip")
        inventory.append("EMP Trap")
        print("\nYou have", inventory, "in your inventory.")
    elif choice4 == "2":
        print("\nYou decide it's too dangerous and leave the area, heading towards the City of Machines.")
    else:
        print("\nInvalid choice. While deciding, another trap is triggered, and you have to flee!")

else:
    print("\nInvalid choice. Please restart the game and select a valid option.")
# This is the dictionary that holds the TV show/Movie title, platform and status.
user_watchlist = {
    "DOCTOR WHO": {
        "Platform": "BBC iPlayer",
        "Status": "Completed",
    },
    "LUCIFER": {
        "Platform": "Amazon Prime",
        "Status": "Completed",
    },    
    "VENOM": {
        "Platform": "Disney+",
        "Status": "Not Watched",
    },
    "TULSA KING": {
        "Platform": "Amazon Prime",
        "Status": "Watching",
    }
}

def add_entry():
    """
    This function asks the user for the title, platform and status of the tv show/movie.
    These details are then added to the user_watchlist dictionary.
    """
    title = input("What is the title of the TV show / Movie: ").strip().upper()  # The title is converted to upper case, to keep it consistent with the entries that are already in the dictionary.
    platform = input("What is the streaming platform: ").strip()

    while True:
        status = input("Status (Not Watched, Watching, Completed): ").strip().lower() # Getting rid of white spaces before and after entry as well as making all the letters lower case.
        if status in ["not watched", "watching", "completed"]:  # Making sure that one of the three acceptable solutions have been entered.
            status = status.title()  # Making the start of each word upper case.
            break  # If the check is successfully complete, break loop so that entry can be added to dictionary.
        else:
            print("Only 'Not watched', 'Watching' and 'Completed' is accepted. Please try again.")

    user_watchlist[title] = {
        "Platform": platform,
        "Status": status,
    }
    print(f"{title} has been added to your watchlist.")

def update_status():
    """
    This function asks the user which title they wish to update the status of.
    If the title is in the watchlist the program will ask for the new status.
    If the title is not in the watchlist, an appropriate message is output.
    """
    title = input("What is the title of the TV show / Movie that needs to be updated: ").strip().upper()
    if title in user_watchlist:
        while True:
            new_status = input("New status (Not Watched, Watching, Completed): ").strip().lower()
            if new_status in ["not watched", "watching", "completed"]:  # Making sure that one of the three acceptable solutions have been entered.
                user_watchlist[title]["Status"] = new_status.title()  # Replacing current status with new status.
                print(f"Updated status of {title} to {new_status.title()}.")
                break
            else:
                print("Only 'Not watched', 'Watching' and 'Completed' is accepted. Please try again.")
    else:
        # If the user selects the update action and the user's entry is not in the watchlist, this message will be output.
        print("The title of the TV show / Movie is not in the watchlist.")


def display_watchlist():
    """
    This function iterates through the user_watchlist dictionary and prints each title along with its details.
    """
    if user_watchlist:
        for title, info in user_watchlist.items():
            print(f"\nTitle: {title}")
            for key, value in info.items():
                print(f"  {key}: {value}")
    else:
        print("Nothing to display. Your watchlist is empty.")


# This is the main menu screen that will continuously ask the user to select an option until they type 'quit'.
# The main menu is displayed at the start and after each action is completed.
while True:
    action = input("\nChoose an action: Add, Update, View, or Quit: ").lower()
    if action == "add":
        add_entry()
    elif action == "update":
        update_status()
    elif action == "view":
        display_watchlist()
    elif action == "quit":
        break
    else:
        print("Please choose Add, Update, View, or Quit.")

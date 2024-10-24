import random
number = random.randint(1,00)
check = 0
while check == 0:
    guessed_number = int(input("Enter a number between 1 and 100: "))
    if 1 <= guessed_number <= 100:
        if guessed_number == number:
            print("You have guessed correctly.")
            check += 1
        else:
            print("Please try again.")
    else:
        print("You must enter an integer between 1 an 100.")
        
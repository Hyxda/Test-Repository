import time
import random
import ninja
import mage

# Custom sleep function
def sleep():
    """
    This function uses the sleep module to set custom
    timing to be reused at various times.
    """
    seconds = 0.5
    time.sleep(seconds)

# Displays game introduction text
def display_intro():
    """
    This function displays a brief introduction of the game
    to the user & takes no parameters.
    """
    print(
    """
    \t \t Welcome to Ninjas vs Mages! \n
    The great war between the ninjas and mages rages on, you must
    choose a side to fight with.
    """
    )

# Gets input from user and saves character selection
def choose_character():
    """
    This function asks the user to input their character selection.
    If an incorrect option is entered by the user, the function is
    recalled till the user has chosen either mage or ninja. Character
    variable is then returned.
    """
    health = 0
    magic = 0
    stealth = 0
    intelligence = 0

    character = ""
    
    while character.lower() != "ninja" or character.lower() != "mage":
        character = input("Who will you join? (Ninja/Mage): \n> ")

        if character.lower() == "ninja":
            health += ninja.ninja_health
            magic += ninja.ninja_magic
            stealth += ninja.ninja_stealth
            intelligence += ninja.ninja_intelligence
            print("\nYou have joined the Ninjas! [{}/{}/{}]".format(magic, stealth, intelligence))
            break

        elif character.lower() == "mage":
            health += mage.mage_health
            magic += mage.mage_health
            stealth += mage.mage_stealth
            intelligence += mage.mage_intelligence
            print("\nYou have joined the Mages! [{}/{}/{}]".format(magic, stealth, intelligence))
            break
        
        else:
            print("\nYou have entered an incorrect option, please retry. ")
            choose_character()
            break

    return character

# Dice Roll
def dice_roll():
    """
    This function uses the "random" module to represent
    two six-sided die. The sum of two die is returned in
    the range of 2 to 12.
    """
    roll = random.randint(2, 12)
    return roll

# Check if user would like to roll the dice.
def role_check():
    win = False
    roll_check = ""
    while win == False:
        roll_check = input("\nWould you like to roll the dice? (Y/N) \n> ")
        if roll_check.lower() == "y":
            roll_result = dice_roll()
            print("\nYou rolled {}!".format(roll_result))
            if roll_result <= 4:
                print("Critical Loss! The game will now end.")
                break
            elif roll_result <= 7:
                print("Loss! The game will now end.")
                break
            elif roll_result <= 10:
                win = True
                print("Win! Moving on to next challenge.")
            elif roll_result <= 12:
                win = True
                print("Ultra Win! Moving on to next challenge.")
            return roll_result
        elif roll_check.lower() == "n":
            print("The game will now end. See you next time!")
            break
        else:
            print("You have entered an incorrect option, please retry.")
            role_check()
            break

# Function calls
display_intro()
sleep()
choose_character()
sleep()
role_check()


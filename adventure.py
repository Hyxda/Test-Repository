import time
import random
import ninja
import mage

# Custom sleep function
def sleep():
    seconds = 0.5
    time.sleep(seconds)

# Displays game introduction text
def display_intro():
    print(
        """
    \t \t Welcome to Ninjas vs Mages! \n
    The great war between the ninjas and mages rages on, you must
    choose a side to fight with.
        """
    )

# Gets input from user and saves character selection
def choose_character():
    health = 0
    magic = 0
    stealth = 0
    intelligence = 0

    character = ""
    while character.lower() != "ninja" or character.lower() != "mage":
        character = input("Who will you join? (Ninja/Mage): ")

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
    return random.randint(2, 12)

# Function calls
display_intro()
sleep()
choose_character()
sleep()

# Clan vs Clan - A Deadly Serious Game!

# Based on the missionaries and cannibals game. Two clans are on one side of a
# void and must cross safely to the other side.  There is only one vehicle and
# it can carry only two beings.  One clan is VERY hungry and if at anytime they
# out number the other clan on either side of the void, they'll eat them.  The
# goal of the game is to make sure that both clans cross the the other side of
# the void in an uneaten state.

import time
import sys

TRUE = 1
FALSE = 0

"""
The traditional game of Missionaries and Cannibal

CALLING = ("missionary", "cannibal")
CLANS = ("missionaries", "cannibals")
CLAN_NAMES_0 = ("Peter", "Paul", "Biff")
CLAN_NAMES_1 = ("Zulu", "Kinta", "Tombalku")
LOCATION = ("Upper Bank", "Lower Bank")
LAUNCH_SITE = "bank"
VEHICLE = "boat"
VEHICLE_FIGURE = "[BOAT]> "
FIRST_BOARDER = "first_boarder"
SECOND_BOARDER = "second_boarder"
"""

"""
An alien variation of the game
"""

CALLING = ("Human", "Alien")
CLANS = ("humans", "aliens")
CLAN_NAMES_0 = ("Tom", "Larry", "Moe")
CLAN_NAMES_1 = ("Zork", "Betel", "Oggs")
LOCATION = ("Planet Zwet", "Planet Earth")
LAUNCH_SITE = "planet"
VEHICLE = "space craft"
VEHICLE_FIGURE = "[=====> "
FIRST_BOARDER = "first"
SECOND_BOARDER = "second"
    
class Being(object):
    """The shell of a man, er ... being"""
               
    upper_level_clan_0 = 0
    upper_level_clan_1 = 0
    lower_level_clan_0 = 0
    lower_level_clan_1 = 0

    @staticmethod
    def census():
        print("There are now \n", \
               Being.upper_level_clan_0, CLANS[0], "and", Being.upper_level_clan_1, CLANS[1], "on the", LOCATION[0], "\n",\
               Being.lower_level_clan_0, CLANS[0], "and", Being.lower_level_clan_1, CLANS[1], "on the", LOCATION[1])
                     
    def __init__(self, calling, name, location=LOCATION[0]):
        self.calling = calling
        self.name = name
        self.location = location
        if self.calling == CALLING[0]:
            Being.upper_level_clan_0 += 1
        else:
            Being.upper_level_clan_1 += 1
        print(self.calling, self.name, "materilaizes on the", LOCATION[0])

    def increment_upper_level_clan_0():
        Being.upper_level_clan_0 += 1

    def decrement_upper_level_clan_0():
        Being.upper_level_clan_0 -= 1

    def increment_lower_level_clan_0():
        Being.lower_level_clan_0 += 1

    def decrement_lower_level_clan_0():
        Being.lower_level_clan_0 -= 1

    def increment_upper_level_clan_1():
        Being.upper_level_clan_1 += 1

    def decrement_upper_level_clan_1():
        Being.upper_level_clan_1 -= 1

    def increment_lower_level_clan_1():
        Being.lower_level_clan_1 += 1

    def decrement_lower_level_clan_1():
        Being.lower_level_clan_1 -= 1
        

def print_population_map(clan_0_list, clan_1_list):

    """
    Show the location of all the players
    """
    
    print("\n")
    print(LOCATION[0], ":", end=" ")
    for i in range(3):
        if clan_0[i].location == LOCATION[0]:
            print(clan_0[i].name, end=" ")
        if clan_1[i].location == LOCATION[0]:
            print(clan_1[i].name, end=" ")

    print("\n-----------------------------------------------------")
    print(LOCATION[1], ":", end=" ")
    for i in range(3):
        if clan_0[i].location == LOCATION[1]:
            print(clan_0[i].name, end=" ")
        if clan_1[i].location == LOCATION[1]:
            print(clan_1[i].name, end=" ")
    print("\n")
    Being.census()
    print("======================================================\n")

def get_passenger(boarding_order):

    """
    Get a passenger (or no one). The passenger must exist in the game and be on the same
    side of the void as the vehicle
    """
    
    need_passenger = TRUE

    while(need_passenger):

        need_passenger = FALSE
        name = None

        # Make sure that only a current named being is selected
        
        while ((name not in CLAN_NAMES_0) and (name not in CLAN_NAMES_1) and name != ""):
            if boarding_order == FIRST_BOARDER:
                name = input("Who should go on board first? ")
            elif boarding_order == SECOND_BOARDER:
                name = input("Who should go on board second (if no one press enter)? ")
            else:
                print("Something is terribly wrong in get_passenger\n")
                
            name = name.title()
            if boarding_order == FIRST_BOARDER and name == "":
                name = None

        # Make sure the selected being is on the same side of the void as the vehicle

        if name != "":

            i = 0
            while ((name != clan_0[i].name) and (name != clan_1[i].name) and i < 3):
                i = i + 1
            if name == clan_0[i].name:
                boarder_location = clan_0[i].location
            else:
                boarder_location = clan_1[i].location
            
            if ((direction == "down" and boarder_location == LOCATION[1]) or \
                (direction == "up") and (boarder_location == LOCATION[0])):
                print(name, "is on the opposite", LAUNCH_SITE, ". \nPick someone on the", \
                      LAUNCH_SITE, "with the", VEHICLE ,".\n")
                name = None
                need_passenger = TRUE

        if name != None:
            return name
    

def cross_the_void(direction, name_1, name_2):

    """
    Get your passengers across the void
    """
    
    print(VEHICLE_FIGURE, end=" ")
    for i in range(3):
        if name_1 == clan_0[i].name or name_2 == clan_0[i].name:
            print(clan_0[i].name, end=" ")
            if direction == "down":
                clan_0[i].location = LOCATION[1]
                Being.decrement_upper_level_clan_0()
                Being.increment_lower_level_clan_0()
            else:
                clan_0[i].location = LOCATION[0]
                Being.increment_upper_level_clan_0()
                Being.decrement_lower_level_clan_0()
    for i in range(3):
        if name_1 == clan_1[i].name or name_2 == clan_1[i].name:
            print(clan_1[i].name, end=" ")
            if direction == "down":
                clan_1[i].location = LOCATION[1]
                Being.decrement_upper_level_clan_1()
                Being.increment_lower_level_clan_1()
            else:
                clan_1[i].location = LOCATION[0]
                Being.increment_upper_level_clan_1()
                Being.decrement_lower_level_clan_1()
    for j in range(10):
        sys.stdout.flush()
        time.sleep(0.2)
        print(end="-")
    print("\n-----------------------------------------------------")


# Main

# Instructions

print("\n\nYOUR ASSIGNMENT")
print("Move every one from", LOCATION[1], "to", LOCATION[0])
print("Use your space craft, which can hold no more than two beings")
print("But remember that", CLANS[1], "like to eat", CLANS[0])
print("Don't let the", CLANS[1], "outnumber the", CLANS[0])
print("on any planet at any time.\n")

# Create the players

clan_0 = [None, None, None]
clan_1 = [None, None, None]

for i in range(3):
    clan_0[i] = Being(CALLING[0], CLAN_NAMES_0[i])

for i in range(3):
    clan_1[i] = Being(CALLING[1], CLAN_NAMES_1[i])

print_population_map(clan_0, clan_1)


# Play the game

direction = None
still_alive = TRUE

while (Being.upper_level_clan_0 + Being.upper_level_clan_1) > 0 and still_alive:

    # Position the vehicle for the next move
    
    if direction == "down":
        direction = "up"
        print("\nThe", VEHICLE, "is on the", LOCATION[1], ".")
    else:
        direction = "down"
        print("\nThe", VEHICLE, "is on the", LOCATION[0], ".")

    # Load the vehicle and cross the void

    name_1 = get_passenger(FIRST_BOARDER)
    name_2 = get_passenger(SECOND_BOARDER)
    cross_the_void(direction, name_1, name_2)

    # Sort out where everyone is and whether anyone has been eaten yet
    
    print_population_map(clan_0, clan_1)

   
    if ((Being.upper_level_clan_0 != 0) and Being.upper_level_clan_0 < Being.upper_level_clan_1) or \
        ((Being.lower_level_clan_0 != 0) and (Being.lower_level_clan_0 < Being.lower_level_clan_1)):
        still_alive = FALSE

# Game over

if still_alive:
    print("Congratulations! You've completed your assignment.\n")
else:
    print("Oh My God! The", CLANS[1], "are eating the", CLANS[0], "! You've lost!\n")
    

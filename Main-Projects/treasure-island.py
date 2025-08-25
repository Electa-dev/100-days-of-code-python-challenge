print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You come to a fork in the road, where do you want to go? ")
left_right = input("\tType 'Left' or 'Right'.\n")
if left_right == "Left" or left_right == "left" or left_right == "LEFT":
    print("You have found a cave!\n")

    print("You went left and found a cave which leads to a beautiful and clear river! Across the river is an island.")
    print("Do you want to swim across or wait? Maybe a boat may come around?")
    swim_wait = input("\tType 'Swim' or 'Wait'\n")
    your_choice = swim_wait.lower()
    if your_choice == "wait":
        print("You decided to be patient and wait! Patience is bitter, but its fruit is sweet!!")
        print("A boat comes along and takes you across to the island.\n")

        print("When you get to the island, you come across a building with three doors.")
        print("To the left is a red door, in the middle is a yellow door and to the right is a blue door.")
        print("Which door will you go through?")
        which_door = input("Type 'Red' for the red door, 'Blue' for the blue door or 'Yellow' for the yellow door.\n")
        chosen_door = which_door.lower()
        if chosen_door == "red":
            print("You go through the red door and enter a tunnel, you walk for sometime then look back but the door has"
                  " disappeared, so you keep on walking.\nYou start to sweat and notice the "
                  "place is getting hotter and hotter til it starts feels like a desert.\nYou see a light up ahead and"
                  " rush towards it, you finally escape the tunnel only to be faced with a desert."
                  "\nWith no water it doesn't take long before you get tired and die of dehydration.\nGAME OVER!")
        elif chosen_door == "yellow":
            print("You go through the yellow door and find yourself in a dimly lit hallway, you look back and the door"
                  " is gone.\nSo you walk across the hallway which seems to stretch on forever. Then you notice some"
                  " doors.\nThere weren't any doors before... you think to yourself. So you try to open them but "
                  "they're locked, so you keep walking and walking.\nAs you walk the passage seems a bit "
                  "darker and the air feels heavy with something sinister.\nYou feel goosebumps on your skin as every "
                  "cell in your body screams for you to run, but you tough it out and look back.\nThen you see a grey"
                  " figure with long claws and a mouth with sharp teeth dripping with saliva.\nYou bolt and just when"
                  " it seems like it's going to get you, you see a door slightly open and run inside.\nLocking the "
                  "door behind you, half expecting the monster to break through you hide under a table in the room.\n"
                  "You hide for a while but nothing happens, so you go to the door and look through the peephole but"
                  " you see nothing.\nThat's when you see a sign on the door that said 'EXIT'.\n"
                  "Excited you look at the table then you see a chest filled with gold and notice another door next to "
                  "a painting on the wall.\nYou carry the chest through the door and find yourself where you began, at "
                  "the sign that said 'welcome to treasure island'.\nYou find a note on th ground that said"
                  " 'CONGRATULATIONS ON SURVIVING, THE GOLD IS YOURS. FEEL FREE TO TRY OUR NEXT CHALLENGE, NO MAN'S "
                  "NEVERLAND.'\nYou've had enough, so you grab your gold and go home, grateful that you were still "
                  "alive.\nYOU WIN!!!!!")
        elif chosen_door == "blue":
            print("The moment you walk through that door, you find yourself in space.\nNo soon than you think 'crap',"
                  " do your lungs rupture and you pass out due to pain and oxygen deprivation.\nYou pass away "
                  "in a few minutes.\nGAME OVER!!!")
        else: print("What's up with you? Can't you spell or listen to instructions?? Gosh, try again.\nYou should be"
                    " grateful I'm nice, if it were the second guardian, he'd have found a way to kick your ass.\n"
                    "GAME OVER, TRY AGAIN!")

    elif your_choice == "swim":
        print("You decide to swim across...bad idea! You get attacked by piranhas and drown!")
        print("Patience is a virtue...guess you weren't virtuous enough!!\nGAME OVER!")
    else:
        print("What's that choice even supposed to be??")
        print("You get pushed into the water and dragged to the bottom by invisible hands and you drown.\nGAME OVER!!!")

elif left_right == "Right" or left_right == "right" or left_right == "RIGHT":
    print("You fell into a hole with spikes!!!\nGAME OVER!")
else:
    print("You fell into a hole with spikes!!!\nGAME OVER!")




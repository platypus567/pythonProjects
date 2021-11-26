print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
input_direction = input("You are at a crossroads. Do you go left or right? \n")
if (input_direction.lower() == "right"):
    print("Walking to the right, you stumble on a mine. Game Over.")
elif (input_direction.lower() == "left"):
    input_swim = input("To the left, you arrive at a lake. Do you swim, or wait for a boat?\n")
    if (input_swim.lower() == "swim"):
        print("Attempting to swim the lake, you get fatigued and drown. Game Over.")
    elif (input_swim.lower() == "wait"):
        input_doors = input("The boat takes you across, and you enter a building on the shore with three doors. One leads to the treasure, the others to certain demise.\n Do you enter the red, green, or blue door?\n")
        if (input_doors.lower() == "red"):
            print("The room was full of men in hockey masks with machetes. You die. Game Over.")
        elif (input_doors.lower() == "green"):
            print("Nothing appears to be wrong at first, but the door to exit suddenly locks. After an hour, the gas kills you. Game Over.")
        elif (input_doors.lower() == "blue"):
            print("The gold shines in front of you. You stuff as much as you can into your sack and leave, victorious. You Win.") 

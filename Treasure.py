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
print("Your mission is to find the treasure and save the princess.") 

#Write your code below this line 👇
first_turn = input("Which way do you want to go? Type 'Left' or 'Right' "). upper()
if first_turn == "LEFT":
    print("Good Choice. Keep going strong")

    second_turn = input("You have reached the River of Life/Death. Do you want to 'swim' or 'wait'? "). upper()
    if second_turn == "WAIT":
        print("I knew I could bet on you to save the princess. Keep going")

        third_turn = input("Now you have to choose 1 door. 'Blue', 'Green' or 'Red'? "). upper()
        if third_turn == "BLUE":
            print("You found the Treasure. You win!")
        else:
            print("You've been held captive. Game over!")

    else:
        print("You got got eaten by the Crocodiles. Game Over!")

else:
    print("You've been devoured by 3 Hungry lions. Game over!")


print("Welcome to Treasure Island!\nYour mission is to find a hidden treasure.")
begin = input('Type "Start" to begin the game: ')
if begin == "Start".lower():
    stage1 = input("You're at a crossroad. Which way would you like to go? Left or Right?")
    if stage1 == "Left".lower():
        stage2 = input("You arrive at a lake. There's an island at the middle of the lake. Type 'Wait' to wait for a boat or 'Swim' to swim to the island: ")
        if stage2 == "Wait".lower():
            stage3 = input("You arrived at the island unharmed. There is a house with 3 doors. One is red, one is blue and one is yellow. Choose a door: ")
            if stage3 == "Red".lower():
                print("You entered a room filled with fire. Game Over!")
            elif stage3 == "Blue".lower():
                print("You entered a room occupied by vicious beasts. Game Over!")
            elif stage3 == "Yellow".lower():
                print("Weldone! You've found the hidden treasure! You Win!")
            else:
                print("You've typed in a wrong option. Try again.")
        elif stage2 == "Swim".lower():
            print("You got eaten by an angry shit. Game Over!")
        else:
            print("You've typed in a wrong option. Try again.")
    elif stage1 == "Right".lower():
        print("You fell into a pit. Game Over!")
    else:
        print("You've typed in a wrong option. Try again.")
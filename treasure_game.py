#a treasure island game
print("welcome to treasure island.")
print("your mission is to find the hidden treasure.")
print("lets get started!!")

choice1 = input("you are at a crossword. where do you want to go? left or right? ").lower()

if choice1 == "left":
    choice2 = input("you are at a river. do you want to swim or wait for a boat? ").lower()
    
    if choice2 == "wait":
        choice3 = input("There's a house here. Time to choose which color door do you want to enter in? yellow, blue or red? ").lower()
        
        if choice3 == "blue":
            print("eaten by ghosts. GAME OVER!")
        elif choice3 == "red":
            print("burnt by fire. GAME OVER!")
        elif choice3 == "yellow":
            print("Congratulations. You won!")
        else:
            print("You chose a door that doesn't exist. GAME OVER!")
    else:
        print("oh no! you got crocodile attacked. GAME OVER!")
else:
    print("Oops! you fell into a hole. GAME OVER!")

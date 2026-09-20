print("Welcome to the Treasure Island.\n Your mission is finding the treasure.")


answer1=input('Youre at the crossroad which side would you like to go? "Right" or "Left?"').lower()
if answer1==("left"):
    answer2=input("You've came to lake would youlike to 'swim'or 'wait'").lower()
    if answer2==("wait"): 
        answer3=input("You' ve arrived to door Which door would you like to open 'blue' or 'red' or 'yellow'").lower()
        if answer3==("yellow"):
            print("You've found the treasure\n CONGRATULATIONS")
        elif answer3==("red"):
            print("You've burned by fire\n GAME OVER ")
            
        elif answer3==("blue"):
            print("You've eaten by beasts\n GAME OVER")

        else:
            print("GAME OVER ")


    else:print("During the lake you've attacked by troute\n GAME OVER  ")

else:print("While going through right side one car hit you!\n GAME OVER")

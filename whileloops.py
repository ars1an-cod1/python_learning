secret=7
attempts=0

while True:
    guess= int(input("Enter a number between 1-10: \n "))
    attempts=attempts +1
    if guess==secret:
        print("Correct!")
        

        print("Attempts count is : \n ",attempts)
        


        break

    elif guess <secret:
        print("Too low!")

        

    else:
        
        print("Too high!")


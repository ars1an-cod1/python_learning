secret=7
attempts=0

while True:
    guess= int(input("Enter a number between 1-10: \n "))

    if guess==secret:
        print("Correct!")
        attempts=attempts +1

        print("Attempts count is : \n ",attempts)
        


        break

    elif guess <secret:
        print("Too low!")

        attempts=attempts +1

    else:
        attempts=attempts+1
        print("Too high!")


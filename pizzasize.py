bill=0
while True:

    size=input("Which size would u like to choose? \n Small , Medium ,Large \n ").lower()

    if size=="small" or size== "medium" or size=="large":
        break
    
    
    print("Invalid size")


if size == "small":
        bill=(8)
        print("Your bill is \n",bill,"$")

elif size=="medium":
        bill=(12)
        print("Your bill is \n",bill, "$")

else:
        bill=(15)
        print("Your bill is \n",bill,"$") 







    

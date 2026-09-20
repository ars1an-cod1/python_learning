    ## ARS PIZZA 

##small == 15$+ 2$(extra pepperoni)
#medıum== 20 $ +3$ (extra pepperoni)
#Large== 25$ +3$(extra pepperoni)
# for everysize extra cheese 1$

print("Welcome to the ARS Pizza ")
bill=0
pizza_size=input("Which size would you like to get ? \n Small, Medium, Large  ").lower()

extra_pepperoni=input("Would you like to get  extra pepperoni? ").lower()
extra_cheese=input("Would you like to get extra cheese? ").lower()

if pizza_size==("small"):
    bill=15
    
elif pizza_size==("medium"):
    bill=20

elif pizza_size==("large"):

    bill=25

else: print(" You typed wrong input.")

if extra_pepperoni==("yes"):
    if pizza_size==("small"):
        bill+=2
    else:bill+=3

if extra_cheese==("yes"):
        bill+=1
       
print("Your pizza bill is ", bill)



## CONDITIONAL STATEMENTS 
print("Welcome to the ACCUMULATOR CAR")
customer_age=int(input ("What's your age? "))
answer=(input(" Are you student?  ")).lower()## keep it as text not bool// as a string if u gonna get input yes or no smth like that you have to use .lower().upper() because of matching string lines 
customer_birthday=(input("Today is it your birthday? ")).lower()
bill=0




if customer_age>=18:


    print("You are allowed the drive accumulator car    ")
    bill=15 
    if answer==("yes") and customer_birthday==("yes"):
        print("You are able to benefited  by our student discount and birthday discount\n Your payment is 5 $")
        bill=5 
    elif answer ==("yes"):## on nested loops 2nd if statement has intendation
        print(" You are able to benefited  by our student discount.\n Your payment is 10$")
        bill=10
    
    
    elif customer_birthday==("yes"):
        print("You're able to benefited our birthday discount \n Your payment is 10 $")
        bill=10

    elif customer_age>=45 and customer_age<=55:
        bill=0
        print("You' re able to get ticket as a free because of midlife crisis discount")

    else: print("  You're not benefited any discounts \n Your payment is 15$    ") 

    customer_photos=input( " Would you like to get professional photos? ").lower()

    if customer_photos==("yes"): 
    ## add their payments 3$
        bill= bill+3 
        
    

    else:print("Your payment is  ", bill)
    
    print("Total payment is",bill)
else: print("You are not allowed the drive accumulator car ")


## == is mean equal to precisely  we use this sign 
## != is mean not equal to literal

## MODULO OPERATOR % ---> It gives remainder after division calculations 10%3=1 , 10%5 = 0 

## Even numbers are able to divided without any remainder 12//6= 2 it is an even number 
## Odd numbers are  which numbers have remainder 

numbers= int(input ("Write a number to check "))
if(numbers%2== 0  ):
    print("Number is an even ")
else: print("Number is a odd")


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
## TREASURE ISLAND PROJECT

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


   



   





 #print('''  ___ _ __   __ _ _ _ __   ___  ___ _ __ 
 #/ _ \ '_ \ / _` | | '_ \ / _ \/ _ \ '__|
#|  __/ | | | (_| | | | | |  __/  __/ |   
 #\___|_| |_|\__, |_|_| |_|\___|\___|_|   
  
  #           __/ |                       
   #         |___/                      
#''')
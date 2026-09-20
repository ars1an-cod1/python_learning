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

def electricbill_calculator(kwh):
    calculation=(kwh*0.15)

    return calculation

def bill_category(amount):

    if amount>=100:
     return("High")
    elif amount >=50:
       return("Medium")

    else:

        return "Low"

kwh_usage=float(input("Enter your kwh usage :"))
result=electricbill_calculator(kwh_usage)
print(bill_category(result))
     
    
    
    # 100+ High, 50+ Medium, altı Low
    
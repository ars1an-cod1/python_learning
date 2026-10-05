## MONTHLY SALARY CALCULATION
#def salary_calc(daily_earning):
 #   result=(daily_earning*30)
    
  #  return result

#daily_earning=int(input("Whats your daily earning"))
#print("Your monthly salary is : ", salary_calc(daily_earning) )


   ## BMI CALCULATION
def bmi_calculation(weight,height):

    calc=(weight/height**2)

    return calc

def bmi_category(value):

    if value>=30:
        print("Obese")
    elif value >=25:
        print("Overweight")
    elif value>=18.5:
        print("Normal")
    else:
       

        return "Underweight "

w=float(input("Weight in kg:"))
h=float(input("Height in meters:"))

result=bmi_calculation(w,h)
print(result)
print(bmi_category(result))
        
#18.5 alti zayif
    #18.5 - 24.9  → Normal
#25 - 29.9    → Overweight
#30 ve üstü   → Obese

    
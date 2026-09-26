def avarage_grade(exam1,exam2,exam3):
    result=(exam1+exam2+exam3)/3

    return result

exam1=int(input("Add your first exam "))
exam2=int(input("Add your second exam"))
exam3=int(input("Add your thirth exam"))

print(avarage_grade(exam1,exam2,exam3)) ## precisely we called to input variables in print function

avg= avarage_grade(exam1,exam2,exam3)


if avg  >=90:
    print("A" )
elif avg >= 80:
    print("B")
elif avg >=70:
    print("C")

elif avg >=60:
    print("D")
else:
    print("F")


##90 and above  → A
##80-89         → B
##70-79         → C
##60-69         → D
#below 60      → F

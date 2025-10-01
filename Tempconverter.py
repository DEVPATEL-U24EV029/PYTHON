temp= float(input("enter the temp  :"))
unit= input("enter the unit is C or F:")
if unit=="C":
    F=(temp*9/5)+32
    print(f"the temperature is: {F} F")
elif unit=="F":
    C=(temp-32)*5/9
    print(f"the temperature is : {C} C")
else:
    print("invalid unit")
    

number = int(input("Enter a number its factorial to be calculated:"))
factorial = 1
if number <0:
    print("Factorial does not exist for negative numbers")
elif number==0:
    print(f"the factorial of {number} is 1")

else:
    for i in range (1, number+1):
        factorial = factorial * i
    print(f"the factorial of {number} is {factorial}")

    


        

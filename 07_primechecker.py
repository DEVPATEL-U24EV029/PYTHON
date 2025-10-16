number=int(input("Enter the number to check whether it is prime or not:"))
if number > 1:
    for i in range (2,number):
        if (number%i==0):
            print(f"{number} is not a prime number")
            break
        else:
            print(f"the number {number} is a prime number")
            break
else:
    print(f"{number} is not a prime number")



   
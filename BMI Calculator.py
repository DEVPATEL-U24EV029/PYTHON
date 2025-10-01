try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.1f}")

    if bmi < 18.5:
        print("You are in the underweight range.")
    elif bmi < 25:
        print("You are in the normal weight range.")
    elif bmi < 30:
        print("You are in the overweight range.")
    else:
        print("You are in the obesity range.")

except ValueError:
    print("Invalid input. Please enter only numbers for weight and height.")
except ZeroDivisionError:
    print("Invalid input. Height cannot be zero.")

def Main():
    height = float(input("What is your height in inches?: "))
    weight = float(input("How much do you weigh in pounds?: "))
    BMI = (weight * 703) / (height * height)
    print("Your BMI is " + str(BMI))

Main()
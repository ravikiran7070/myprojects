#BMI Calculator
print("Welcome to the BMI calculator!")
#Declare a variable with float datatype for weight
weight = float(input("What is your weight in kg? "))
#Declare a variable with float datatype for height
height = float(input("What is your height in metres? "))
#Declare a variable to calculate the BMI
bmi = float(weight / (height ** 2))
#Print the BMI for the user to convert bmi to string to concatenate
print ("Your BMI is : " + str(round(bmi,2)))
#write the If else elif statements to display different scenarios.
if bmi <= 18.5:
        print("You are underweight")
elif bmi <= 25:
        print("You are normal weight")
elif bmi > 25:
        print("You are normal weight")

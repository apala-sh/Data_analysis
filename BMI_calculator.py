# BMI = (weight in kg)/(height in m)^2

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
BMI = (weight) / (height**2)
print(BMI)
if (BMI<18.5):
    print("Underweight")
elif (18.5 <= BMI <= 24.9):
    print("Healthy weight")
elif (25 <= BMI <= 29.9):
    print("Overweight")
elif (BMI>=30):
    print("Obese")
else:
    print("Enter valid inputs")
# Calculates and checks BMI

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
I = (weight / (height) ** 2)
BMI = round(I,2)
if BMI <= 18.5:
    print(f"Your bmi is {BMI} and you are underweight")
elif BMI <=25:
    print(f"Your bmi is {BMI} and you have normal weight")
elif BMI <=30:
    print(f"Your bmi is {BMI} and you are overweight")
elif BMI <= 35:
    print(f"Your bmi is {BMI} and you are obese")
else:
    print(f"Your bmi is {BMI} and you are clinically obese")

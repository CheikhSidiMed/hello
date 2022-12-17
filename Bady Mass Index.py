weight = float(input("Enter your weight en kg: "))
height = float(input("Enter your height en cm: "))
BMI = weight / (height/100)**2

if BMI < 18.5 :
    message = "Underweight"
elif BMI < 25 :
    message = "Healthy"
elif BMI < 30 :
    message = "Overweight"
elif BMI >= 30 :
    message = "Obese"

print(message)

# BMI Calculator
# Enter your weight and height to calculate your BMI
# ---------

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
height = height / 100
BMI_number = (weight / (height ** 2))

def BMI_Calculator(BMI_number):
    print (BMI_number)
    BMI_number = int(BMI_number)
    if BMI_number < 18.5:
        return "Underweight"
    elif 18.5 <= BMI_number <= 24.9:
        return "Normal weight"
    elif 25 <= BMI_number <= 29.9:
        return "Overweight"
    elif 30 <= BMI_number <= 34.9:
        return "Medical obesity (I)"
    elif 35 <= BMI_number <= 39.9:
        return "Medical obesity (II)"
    elif BMI_number >= 40:
        return "Extreme obesity (III)"
    
print(BMI_Calculator(BMI_number))

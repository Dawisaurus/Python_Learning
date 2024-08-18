"""Exercise 1: Calculate the Area of a Triangle
Write a Python program that calculates the area of a triangle. The program should:
Take the base and height of the triangle as inputs from the user.
Compute the area using the formula: Area = 0.5 * base * height.
Output the result to the user."""

# Exercise 1
# Todo: 1) Input base & height of traingle from user 2) I will convert the base strings from input to float
#       3) Use Formula to get Triangle's area 4) Print the result

triangle_base = float(input("Enter triangle's base: "))
triangle_height = float(input("Enter triangle's height: ")) 
triangle_area = 0.5 * triangle_base * triangle_height
print("Triangle's area is:", triangle_area)

#-------------------------------------------------------#

"""Exercise 2: Find the Largest of Three Numbers
Write a Python program that takes three numbers as input from the user and determines which one is the largest.
Make sure to handle cases where some or all numbers are equal."""

# Exercise 2
# Todo: 1) Input 3 numbers from user, I'll call them A, B, C 2) I will convert the base strings to float
#       3) I'll make program determine which is the highest using max() if one is highest, and ill use if/elif
#       To go over more possible combinations (A-B) (A-C) (B-C) to handle cases where some or all numbers are equal
#       4) Print results

A = float(input("First number: "))
B = float(input("Second number: "))
C = float(input("Third number: ")) 

if A == B == C:
    highest_number = (A, B, C)
elif A == B:
    if A > C:
        highest_number = (A, B)
    else:
        highest_number = C 
elif A == C:
    if A > B:
        highest_number = (A, C)
    else:
        highest_number = (B)
elif B == C:
    if B > A:
        highest_number = (B, C)
    else:
        highest_number = (A)
else:
    highest_number = max(A, B, C)
print("The highest number or numbers are:", highest_number)

 
#-------------------------------------------------------#

"""Exercise 3: Temperature Conversion
Write a Python program that converts a temperature from Fahrenheit to Celsius and vice versa. The program should:
Take the temperature and the unit (F or C) as inputs from the user.
Convert the temperature to the other unit.
Output the result to the user."""
# Exercise 3
# Todo: 1) Input Temperature and Unit and assign to variables 
#       2) Use formula (32°F − 32) * 5/9 = 0°C F>C / C>F (0°F * 9/5) + 32 = 32°C
#       3) Convert to opposite unit F>C / C>F 4) Print result

temperature = float(input("Temperature: "))
unit = input("Of which unit? [Fahrenheit/Celsius]: ").lower()
if unit == "fahrenheit":
    result_temperature = (temperature - 32) * 5/9
elif unit == "celsius":
    result_temperature = (temperature * 9/5) + 32
print (result_temperature)

#-------------------------------------------------------#

"""Exercise 4: Simple Interest Calculator
Write a Python program to calculate the simple interest. The program should:
Take the principal amount, annual interest rate, and time in years as inputs from the user.
Compute the simple interest using the formula: Simple Interest = Principal * Rate * Time.
Output the result to the user."""
# Exercise 4
# Todo: 1) Input Principal, Interest Rate as % percentage and Time in years and 
#       2) I will assign them to variables and convert into float
#       3) Use formula (Interest = Principal * Rate * Time)
#       4) Lastly print
principal_ammount = float(input("Principal ammount: "))
interest_rate_percent = float(input("Interest rate %: "))
time_in_years = float(input("Time in years: "))
interest_rate_percent = interest_rate_percent / 100

result = principal_ammount * interest_rate_percent * time_in_years
print("Interest is:", result)

#-------------------------------------------------------#

"""Exercise 5: Sum of Digits
Write a Python program that takes a three-digit number as input and calculates the sum of its digits. 
For example, if the input is 456, the output should be 15 (4 + 5 + 6)."""
# Exercise 5
# Todo: 1) Input three digit number and assign it to variable
#       2) I will check if input is 3 characters, specifically digit long using len() and .isdigit()
#       3) Ill convert them into int and sum them one by one using 'for'
#       4) Lastly print result
while True:
    number = input("Enter 3 digit number: ")
    if len(number) == 3 and number.isdigit():
        summed = sum(int(digit) for digit in number)
        print("Sum of digits: ", summed)
        break
    else:
        print("Incorrect input, enter 3 digit number")

#-------------------------------------------------------#
#                   August 10th 2024                    #
#-------------------------------------------------------#

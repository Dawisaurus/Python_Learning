"""Exercise 1: Determine the Largest of Three Numbers
Write a Python program that takes three numbers as input and determines the largest number."""

# Exercise 1
# Todo: 1) I'll take input of 3 numbers and assign each of them to a different variable
#       2) Change strings into int
#       3) I'll use max() for program to figure out largest number out of them
#       4) Finally use print()
#       5*) I'll identify which variable has the highest number 

A = int(input("First number: "))
B = int(input("Second number: "))
C = int(input("Third number: "))
largest_number = max(A, B, C)
if largest_number == A:
    print(f"Largest number is A -", largest_number)
elif largest_number == B:
    print(f"Largest number is B -", largest_number)
else:
    print(f"Largest number is C -", largest_number)

#-------------------------------------------------------#

"""Exercise 2: Check if a Number is Positive, Negative, or Zero
Write a Python program that checks if a number is positive, negative, or zero and prints a message accordingly."""

# Exercise 2
# Todo: 1) I'll take an input of a single number and make it an integer
#       2) Number is positive if number >0 
#       3) Number is negative if number <0
#       4) Number is zero if number == 0
#       5) Lastly I'll print number and message whether its positive, negative or zero

number = int(input("Enter a number: "))
if number > 0:
    print(number, "is a positive number!")
elif number < 0:
    print(number, "is a negative number!")
elif number == 0:
    print(f"the number is {number}!")
else:
    print("Error")

#-------------------------------------------------------#

"""Exercise 3: Grade Classification
Write a Python program that takes a numeric grade (0 to 100) and prints the corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F"""

# Exercise 3
# Todo: 1) I'll take an input and assign it to 'numeric_grade' variable and convert it to integer
#       2.1) if grade >= 90, letter_grade = A
#       2.2) if grade in range (80, 90), letter_grade = B
#       2.3) if grade in range (70, 79), letter_grade = C
#       2.4) if grade in range (60, 69), letter_grade = D
#       2.5) if grade < 60 (I'll use else), letter_grade = F
#       3) Lastly print letter grade

numeric_grade = int(input("Enter your numeric grade: "))
if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade in range (80, 90):
    letter_grade = "B"
elif numeric_grade in range (70, 80):
    letter_grade = "C"
elif numeric_grade in range (60, 70):
    letter_grade = "D"
else:
    letter_grade = "F"
print (letter_grade)

#-------------------------------------------------------#

"""Exercise 4: Check Leap Year
Write a Python program that determines if a given year is a leap year or not. A year is a leap year if:
It is divisible by 4,
but not divisible by 100, unless it is also divisible by 400."""

# Exercise 4
# Todo: 1) I'll take an input and assign it to 'year' variable and convert it to integer
#       2) I'll use '%' to get whatever remains from division
#       3) If year is divisible by 400 & 4 it IS a lap year, if its divisible by 100 or not divisible by 4 it IS NOT a lap year
#       4) Lastly print the result whether it is a lap year or not
year = int(input("Year: "))
if year == 0:
    print("There's no such thing as year 0!")
if year % 400 == 0:
    print(f"Year {year} is divisible by 400, it is a lap year!")
elif year % 100 == 0:
    print(f"Year {year} is divisible by 100, it isn't a lap year!")
elif year % 4 == 0:
    print(f"Year {year} is divisible by 4, it is a lap year!")
else:
    print(f"Year {year} is not divisible by 4, it isn't a lap year")

#-------------------------------------------------------#

"""Exercise 5: Determine the Type of Triangle
Write a Python program that takes the lengths of the three sides of a triangle as input
and determines if the triangle is equilateral, isosceles, or scalene."""

# Exercise 5
# Todo: 0.0) There are 3 types of triangles 
#       0.1) Equilateral Triangle: Where all three sides are equal. [3 sides == sides]
#       0.2) Isosceles Triangle: Where two sides are equal. [2 sides == sides]
#       0.3) Scalene Triangle: Where all sides are different. [0 sides == sides]
#       1) I'll take an input for 3 sides and assign them to variables and convert them into float
#       2.1) It's Equilateral Triangle if side1 == side2 == side
#       2.2) It's Isosceles Triangle if side1 == side2 or side1 == side3 or side2 == side3
#       2.3) It's Scalene triangle if side1 != side2 and  side1 != side3 and side2 != side3
#       3) Lastly determine and print which type of triangle would that be

side1 = float(input("Number for first side: "))
side2 = float(input("Number for second side: "))
side3 = float(input("Number for third side: ")) 
if side1 == side2 == side3:
    triangle_type = "Equilateral Triangle"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles Triangle"
elif side1 != side2 and side1 != side3 and side2 != side3:
    triangle_type = "Scalene Triangle"
else:
    print("Error")
print("Triangle in question is", triangle_type)

#-------------------------------------------------------#
#                   August 10th 2024                    #
#-------------------------------------------------------#
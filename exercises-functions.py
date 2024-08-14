"""Exercise 1: Function with Default Parameters
Task: Write a function describe_pet(pet_name, pet_type='dog') that takes two parameters: 
pet_name and pet_type (with a default value of 'dog').
The function should print a message describing the pet, e.g., "My pet is a dog named Rover."""

# Exercise 1
# Todo: 1) I will start with function called describe_pet 2) Function will use input to take 2 parameters: 
#       name & type of a pet 3) Function will print both parameters in a sentence 4) Lastly I'll call the function

def describe_pet():
    pet_name = input("Pet name: ")
    pet_type = input("Pet type: ")
    print(f"My pet is a {pet_type} named {pet_name}")

describe_pet()

"""Exercise 2: Keyword Arguments
Task: Write a function print_book_info(title, author, year_published) 
that takes required parameters (title, author, year_published). 
The function should print all provided information about a book."""

# Exercise 2
# Todo: 1) I will make function called print_book_info
#       2) I will take 3 parameters using unput: info, title, author
#       3) Lastly I'll call the function

def print_book_info(title, author, year_published):
    info = (f"Book Info:\n Title: {title}\n Author: {author}\n Year Published: {year_published}")
    print ()
    print (info)

title = input("Title: ")
author = input("Author: ")
year_published = input("Year published: ")

print_book_info(title, author, year_published)

"""Exercise 3: Find the Maximum Task: Write a function find_max 
that takes a list of numbers as a parameter and returns the maximum value in the list."""

# Exercise 3
# Todo: 1) I will make function called find_max
#       2) I will take multiple parameters using unput
#       3) I'll convert the input into float numbers and add them to list using .append()
#       4) Lastly I'll call the function and print the highest number

def find_max(numbers):
    return max(numbers)

user_input = input("Type numbers separated by space: ")
number_list = [] 
for num in user_input.split():
    number_list.append(float(num))
print(f"The highest number is {find_max(number_list)}")

"""Exercise 4: Even or Odd Task: 
Write a function is_even that takes an integer as a parameter 
and returns True if the number is even and False if it is odd."""

# Exercise 4
# Todo: 1) I will start with function is_even
#       2) If number 2 remainder is equal 0, then number is even, else it's odd
#       3) I will take user input as int
#       4) I will call function and use parameter given by user as user_input

def is_even(number):
    if number % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
    
user_input = int(input("Your number: "))
print (is_even(user_input))

"""Exercise 5: Sum of Two Numbers
Task: Write a function add_numbers that takes two numbers as parameters and returns their sum."""

# Exercise 5
# Todo: 1) I will start with function add_numbers
#       2) Function will take 2 numbers using input by user
#       3) Function will return those 2 given numbers as a sum
#       4) Lastly it will print the sum

def add_numbers(numberfirst, numbersecond):
    return (numberfirst + numbersecond)

numberfirst = int(input("Your first number: ")) 
numbersecond = int(input("Your second number: "))
print (add_numbers(numberfirst, numbersecond))

"""Exercise 6: Calculate Average
Task: Write a function calculate_average
that takes a list of numbers and returns their average."""

# Exercise 6
# Todo: 1) I will start with function calculate_average
#       2) Function will take numbers using input by user
#       3) Function will return all the numbers as a sum of numbers, divided by length
#       4) Lastly print the average
def calculate_average(number_list):
    return sum(number_list) / len(number_list)


user_input = input("Use numbers separated by space: ")
number_list = [int(number) for number in user_input.split()]

print (calculate_average(number_list))


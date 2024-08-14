# A simple calculator in Python 
while True:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    operator = input("+ , - , * , / , or 'exit': ")
    if operator == "exit":
        break
    elif operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        if y != 0:
            result = x / y
        else:
            print("Can't divide by zero")
            continue
    else:
        print("Error")
        continue
    print("The result is:", result)

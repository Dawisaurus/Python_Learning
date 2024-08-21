x = 0
y = 1
z = 0
limit = int(input("Fibonacci sequence limit: "))
while True:
    z = x + y
    x = y
    y = z
    print(z)
    if z > limit:
        break
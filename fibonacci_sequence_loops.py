# Enter the limit for fibonacci sequence to start it
# 
# 
# 
x = 0
y = 1
z = 0
limit = int(input("Fibonacci sequence limit: "))
for i in range (1, limit):
    z = x + y
    x = y
    y = z
    print(z)
    if i == limit:
        break
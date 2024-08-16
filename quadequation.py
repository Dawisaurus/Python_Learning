# This script solves the Quadratic equation 
# User intputs 3 numbers assigned to A, B & C variables

import math

x = int(input("Letter A: "))
y = int(input("Letter B: "))
z = int(input("Letter C: "))

# These are calculated using quadratic formula: Ax^2 + Bx + C
def qfunction(A, B, C):
    delta = ((B * B) - 4*A*C)
    if delta == 0:
        return ((-B) / (2 * A))
    elif delta > 0:
        x1 = ((-B) - math.sqrt(delta)) / (2 * A)
        x2 = ((-B) + math.sqrt(delta)) / (2 * A)
        return (x1, x2)
    elif delta < 0:
        return "no result"
    else:
        return "error"

# Lastly the result is printed, there are 4 possible outcomes:
# 1 Two roots 
# 2 One root 
# 3 No root
# 4 Error
print (qfunction(x, y, z))

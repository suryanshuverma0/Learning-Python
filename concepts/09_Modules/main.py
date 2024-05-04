import math_expression
from math_expression import add as additon
from math_expression import subtract as substraction

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))

additionResult = additon(a, b)
substractionResult = substraction(a, b)
print(additionResult)
print(substractionResult)

# Task 2: Using the Math Module for Calculations

import math

num = float(input("Enter a number: "))

print("Square root: ", math.sqrt(num))
if num > 0:
    print("logarithm: ", math.log(num))
else:
    print("Logarithm is not defined for zero or negative numbers.")

print("Sine: ", math.sin(num))

import math

# Constants
print("Value of π (pi):", math.pi)
print("Value of e:", math.e)

# Basic Arithmetic
print("Square root of 25:", math.sqrt(25))
print("2 raised to the power 3:", math.pow(2, 3))
print("Exponential of 2:", math.exp(2))
print("Natural logarithm of 10:", math.log(10))

# Trigonometry
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print("Sine of", angle_degrees, "degrees:", math.sin(angle_radians))
print("Cosine of", angle_degrees, "degrees:", math.cos(angle_radians))
print("Tangent of", angle_degrees, "degrees:", math.tan(angle_radians))

# Hyperbolic Functions
x = 1
print("Hyperbolic sine of", x, ":", math.sinh(x))
print("Hyperbolic cosine of", x, ":", math.cosh(x))
print("Hyperbolic tangent of", x, ":", math.tanh(x))

# Angular Conversion
print("Inverse sine of 0.5:", math.degrees(math.asin(0.5)))
print("Inverse cosine of 0.5:", math.degrees(math.acos(0.5)))
print("Inverse tangent of 1:", math.degrees(math.atan(1)))
print("Arc tangent of (1, 1):", math.degrees(math.atan2(1, 1)))

# Miscellaneous
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.9:", math.floor(4.9))
print("Absolute value of -5:", math.fabs(-5))
print("Factorial of 5:", math.factorial(5))
print("GCD of 15 and 20:", math.gcd(15, 20))

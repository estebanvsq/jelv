# 1

name = input("Enter your name: ")
print(f"¡Hello!, {name}")

# 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"The sum of {num1} and {num2} is {num1 + num2}")

# 3

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# 24

days = float(input("Enter the number of days you want to switch to seconds: "))

print(f"{days} days are {days * 24 * 60 * 60} seconds")

# 23

mass_kg = float(input("Enter the mass in kilograms: "))
velocity_ms = float(input("Enter the velocity in meters per second: "))

print(f"The kinetic energy is: {0.5 * mass_kg * velocity_ms ** 2} Joules")

# 22

number = float(input("Enter a number to know if its positive, negative or zero: "))

positive = number > 0
negative = number < 0
zero = number == 0

print(f"""Is positive? {positive}
Is negative? {negative}
Is zero? {zero}
""")

# 21

price = (float(input("Enter the price of the product: "))) * 1.19
discount_percentage = float(input("Enter the discount percentage: "))
discount_amount = (discount_percentage / 100) * price
print(f"The final price after a discount of {discount_percentage}% is: {price - discount_amount}")

# 20

age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))

print(f"""The sum of both ages is: {age1 + age2}
The first person is older than the second? → {age1 > age2}""")

# 19

str_input = input("Enter a string: ")
print(f"The length of the string is: {len(str_input)}")

# 18

from math import pi

radius = float(input("Enter the radius of the circle: "))
print(f"""The area of the circle with radius {radius} is: {pi * radius ** 2}
The perimeter of the circle with radius {radius} is: {2 * pi * radius}""")

# 17

coef_a = float(input("Enter coefficient a: "))
coef_b = float(input("Enter coefficient b: "))

if coef_a != 0 or coef_b != 0:
    print(f"The solution for 'x' is: {-coef_b / coef_a}")
else:
    print("Error: Coefficient 'a' cannot be zero.")

# 16

kg = float(input("Enter weight in kilograms: "))
height_m = float(input("Enter height in meters: "))

imc = kg / (height_m ** 2)
print(f"The Body Mass Index (IMC) is: {round(imc, 2)}")

# 15

from math import log

numlog = float(input("Enter a positive number to calculate its natural logarithm: "))

if numlog > 0:
    print(f"The natural logarithm of {numlog} is: {log(numlog)}")
else:
    print("Error: Cannot compute the logarithm of a non-positive number.")

# 14

# 13

# 12

cat1 = float(input("Enter the length of the first leg of the right triangle: "))
cat2 = float(input("Enter the length of the second leg of the right triangle: "))
print(f"The length of the hypotenuse is: {(cat1 ** 2 + cat2 ** 2) ** 0.5}" )

# 11

# 10

# 9

# 8

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

print(f"""The sum of {input1} and {input2} is {input1 + input2}
The difference between {input1} and {input2} is {abs(input1-input2)}""")

# 7

celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius}°C is equal to {celsius * 9 / 5 + 32}°F")

# 6


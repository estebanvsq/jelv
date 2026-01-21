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
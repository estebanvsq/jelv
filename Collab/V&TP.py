num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

calc = input("""Input a character depending in what calculation you want to do:
x → Multiply
/ → Divide
+ → Add
- → Subtract

Your choice: """)

while calc not in ["x", "/", "+", "-"]:
    print("Invalid operation selected. Please try again.")
    calc = input("""Input a character depending in what calculation you want to do: 
x → Multiply
/ → Divide 
+ → Add
- → Subtract
                 
Your choice: """)
    
if calc == "x":
    result = num1 * num2
    print(f"The result of {num1} x {num2} is {result}")
elif calc == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif calc == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
else:
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
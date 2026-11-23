#Build a command-line calculator that accepts two numbers and performs basic mathematical operations based on the operator selected by the user.

num1 = float(input("Enter first number : "))
operator = input("Enter operator : ")
num2 = float(input("Enter second number : "))

print("Calculating...")

def calculator(a,operator,b):
  if operator == "+":
    return a + b
  elif operator == "-":
    return a - b
  elif operator == "*":
    return a * b
  elif operator == "/":
    if b == 0:
      return "Error: Cannot divide by zero."
    return a / b
  else:
    return "Error: Invalid operator.\nSupported operators are '+' , '-' , '*' , '/' "

print(f"Result : {calculator(num1,operator,num2)}")

#improved code in 02-calc.py
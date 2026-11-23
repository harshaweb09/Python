#handling operator validation

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

while True:
  operator = input("Enter operator : ")
  valid_operators = ("+","-","*","/")
  if operator  in valid_operators:
    break
  else:
    print("Invalid operator! Please enter one of +, -, *, /.")

while True:
  try:
    num1 = float(input("Enter first number : "))
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")

while True:
  try:
    num2 = float(input("Enter second number : "))
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")

print("Calculating...")

print(f"Result : {calculator(num1,operator,num2)}")

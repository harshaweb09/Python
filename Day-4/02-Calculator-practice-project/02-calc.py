#Handling non numeric inputs using try and except

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
  try:
    num1 = float(input("Enter first number : "))
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")
operator = input("Enter operator : ")
while True:
  try:
    num2 = float(input("Enter second number : "))
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")

print("Calculating...")


print(f"Result : {calculator(num1,operator,num2)}")

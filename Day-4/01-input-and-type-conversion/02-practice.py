#Ask for two numbers and print their sum.
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
sum = num1 + num2
print(f"Sum of {num1} and {num2} is : {sum}")

#typeconversion from string to int
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
sum = num1 + num2
print(f"Sum of {num1} and {num2} is : {sum}")

#Ask for a user's age and determine whether they are eligible for an adult account (18 or older).
age = int(input("Enter your age : "))
if age >= 18 :
  print("You are eligible for individual account")
else :
  print("You need to be at least 18 years old to be eligible for an individual account")

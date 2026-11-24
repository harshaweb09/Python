#Student Grade Calculator
def input_and_validate_number(subject):
  while True:
    try:
      mark = float(input(f"Enter {subject} marks : "))
      if mark >= 0 and mark <= 100:
        return mark
      else:
        print("RangeError: Invalid marks entered! Enter a valid marks from 0 to 100")
    except ValueError:
      print("ValueError: Invalid marks entered! Enter a valid marks from 0 to 100")

subjects = ("English","Mathematics","Science","Social Studies","Computer Science")

marks = {}

name = input("Enter your name : ")

for subject in subjects:
  marks[subject] = input_and_validate_number(subject)

print(marks)



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

def total_marks(subjects):
  total = 0
  for marks in subjects.values():
    total += marks
  return total

subjects = ("English","Mathematics","Science","Social Studies","Computer Science")

marks = {}

name = input("Enter your name : ")

for subject in subjects:
  marks[subject] = input_and_validate_number(subject)

print(marks)
print(f"Total Marks: {int(total_marks(marks))}/500")



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

def total_marks_obtained(marks):
  total = 0
  for mark in marks.values():
    total += mark
  return total

def actual_total_marks(marks):
  return len(marks)*100

def average(marks):
  return (f"{(total_marks_obtained(marks)/actual_total_marks(marks))*100}%")

def check_pass_fail(marks):
  for mark in marks.values():
    if mark < 35:
      return "FAIL"
  return "Pass"

subjects = ("English","Mathematics","Science","Social Studies","Computer Science")

student_marks = {}

name = input("Enter your name : ")

for subject in subjects:
  student_marks[subject] = input_and_validate_number(subject)

print(student_marks)
print(f"Total Marks: {int(total_marks_obtained(student_marks))}/{actual_total_marks(student_marks)}")
print(average(student_marks))
print(check_pass_fail(student_marks))
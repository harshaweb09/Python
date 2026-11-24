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
  return (total_marks_obtained(marks)/actual_total_marks(marks))*100

def check_pass_fail(marks):
  for mark in marks.values():
    if mark < 35:
      return "FAIL"
  return "Pass"

def grade_calculator(is_passed,percentage):
  if is_passed == "FAIL":
    return "F"
  else:
    if percentage >= 90:
      return "A"
    elif percentage >= 80 and percentage < 90:
      return "B"
    elif percentage >= 70 and percentage < 80:
      return "C"
    elif percentage >= 60 and percentage < 70:
      return "D"
    elif percentage >= 50 and percentage < 60:
      return "E"
    else:
      return "F"    
    
subjects = ("English","Mathematics","Science","Social Studies","Computer Science")

student_marks = {}

name = input("Enter your name : ")

for subject in subjects:
  student_marks[subject] = input_and_validate_number(subject)

print(student_marks)
print(f"Total Marks: {int(total_marks_obtained(student_marks))}/{actual_total_marks(student_marks)}")
print(average(student_marks))
print(check_pass_fail(student_marks))
print(grade_calculator(check_pass_fail(student_marks),average(student_marks)))
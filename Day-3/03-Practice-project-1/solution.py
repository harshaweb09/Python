#Student Marks Analyzer

# marks = [85, 76, 92, 68, 89]
marks = []

def total_marks(marks) :
  total = 0
  for mark in marks :
    total += mark
  return total

print("Total : ",total_marks(marks))

def avg_marks(marks) :
  if len(marks) == 0 :
    return None
  total = total_marks(marks)
  count = len(marks)
  return (total/count)

print("Average : ",avg_marks(marks))

def highest_mark(marks) :
  if len(marks) == 0 :
    return None
  highest = marks[0]
  for mark in marks :
    if mark > highest :
      highest = mark
  return highest
  
print("Highest : ",highest_mark(marks))

def is_passed(marks) :
  if avg_marks(marks) == None:
  # if avg_marks(marks) is None:
    return "No marks available"
  if avg_marks(marks) >= 40 :
    return "Passed"
  else :
      return "Failed"

print("Result : ",is_passed(marks))
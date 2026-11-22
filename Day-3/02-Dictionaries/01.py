student = {
  "id":101,
  "name":"vardhan",
  "age":21,
  "course":"BCA"
}
print(student)

# accessing
print(student["name"])

# adding
student["percentage"] = 90
print(student)

#updating
student["name"]="Harsha"
print(student)

# deleting items
del student["percentage"]
print(student)

#pop
print(student.pop("course"))

#get accesing values without causing an error 
print(student.get("course"))
print(student.get("age"))

#clear all items 
print(student.clear())
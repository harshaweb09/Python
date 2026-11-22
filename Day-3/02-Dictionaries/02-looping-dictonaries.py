student = {
  "id":101,
  "name":"vardhan",
  "age":21,
  "course":"BCA"
}

#looping through dictonary keys
for key in student :
  print(key)
  
#looping through dictonary values
for value in student.values() :
  print(value)
  
#looping through keys and values
for key,value in student.items() :
  print(key," : ",value)

users = {"ravi","ashok","Siva","rahul","martin","ravi","ashok"}

#adding single element using add()
users.add("peter")
print(users)

#adding multiple items using update()
users.update(["rakesh","chandu"])
print(users)

#to remove random element pop()
print(users.pop())

#to remove specific element,if not exists throws an error
users.remove("ravi")
print(users)
# print(users.remove("ravi"))

#to remove specific element,if not exists doesnot throws an error
users.discard("siva")
# print(users.discard("siva"))


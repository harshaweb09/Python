#Creating a list

languages = ["python","c","java","c++","php"]

print(languages)

#Print the third item from that list.

print(languages[2])

# add 'JavaScript' to the end of the list.

languages.append("Javascript")

print(languages)

#Change the first item to 'Perl'.
languages[0] = "Perl"
print(languages)

# Print every item using a for loop.

for language in languages : 
  print(language)

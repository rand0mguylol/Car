# Read the whole file as a single string
with open("admin.txt", "r") as af:
  l = af.read()
  print(l)


# Loop through each line
with open("admin.txt", "r") as af:
  for l in af:
    print(l.strip())

# Returns a list
# Each line is an element in the list
with open("admin.txt", "r") as af:
  l = af.readlines()
  print(l)


# Returns a list of list
# Each line is a list in the outer list
# Each column is an element in the inner list
file_list = []
with open("admin.txt", "r") as rf:
  for lines in rf:
    temp_list = []
    lines_list = lines.split("     ")
    for element in lines_list:
      if element != "":
        element = element.strip()
        temp_list.append(element)
    
    file_list.append(temp_list)

# print(file_list)

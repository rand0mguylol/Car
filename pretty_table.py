# from format_file_list import format_file_list

# Integrates wirh format_file_list
# The file_list parameter accepts a list of list
# format_file_list returns a a list of list

from format_file_list import format_file_list


# def pretty_table(filename, file_list):  
#   # Get the max length of the string in each column
#   max_length_list = []
#   max_length = 0

#   col = 0
#   while col < len(file_list[0]):
#     for row in file_list:
#       if max_length < len(row[col]):
#         max_length = len(row[col])
    
#     max_length_list.append(max_length)
#     max_length = 0
#     col += 1
   
#   # Reformat and wrtie back to the file based on the new max length
#   with open(filename, "w") as af:
#     final_text = ""
#     t = 0 
#     while t < len(file_list):
#       for col in range(len(file_list[t])):
#         for length in range(len(max_length_list)):
#           if col == length:
#             test = f"{file_list[t][col].ljust(max_length_list[length] + 5)}"
#             final_text += test
#             break

#       final_text += "\n"
#       t +=1     
#     af.write(final_text)


# file_list accepts a list of list only
# def pretty_table_display(file_list, column_index = None):
#   # file_list = format_file_list.format_file_list(filename)
  
#   # Get the max length of the string in each column
#   max_length_list = []
#   max_length = 0
#   col = 0
#   while col < len(file_list[0]):
#     for row in file_list:
#       if max_length < len(row[col]):
#         max_length = len(row[col])
    
#     max_length_list.append(max_length)
#     max_length = 0
#     col += 1

#   # Reformat and wrtie back to the file based on the new max length
#   final_text = ""
#   t = 0 
#   while t < len(file_list):
#     for col in range(len(file_list[0])):
#       for length in range(len(max_length_list)):
#         if column_index == None or col != column_index:
#           if col == length:
#             text = f"{file_list[t][col].ljust(max_length_list[length] + 5)}"
#             final_text += text
#             break

#     final_text += "\n"
#     t +=1     

#   print(final_text)




# def pretty_table_display(file_list, column_index = None):
#   # file_list = format_file_list.format_file_list(filename)
  
#   # Get the max length of the string in each column
#   max_length_list = []
#   max_length = 0
#   col = 0
#   while col < len(file_list[0]):
#     for row in file_list:
#       if max_length < len(row[col]):
#         max_length = len(row[col])
    
#     max_length_list.append(max_length)
#     max_length = 0
#     col += 1

#   # Reformat and wrtie back to the file based on the new max length
#   final_text = ""
#   t = 0 
#   while t < len(file_list):
#     for col in range(len(file_list[0])):
#       for length in range(len(max_length_list)):
#         if column_index == None or col not in column_index:
#           if col == length:
#             text = f"{file_list[t][col].ljust(max_length_list[length] + 5)}"
#             final_text += text
#             break

#     final_text += "\n"
#     t +=1     

#   print(final_text)

  

def pretty_table_display(file_list, column_index = None):
  # file_list = format_file_list.format_file_list(filename)
  
  # Get the max length of the string in each column
  max_length_list = []
  max_length = 0
  col = 0
  
  while col < len(file_list[0]):
    for row in file_list:
      if max_length < len(row[col]):
        max_length = len(row[col])
    
    max_length_list.append(max_length)
    max_length = 0
    col += 1

  # Reformat and wrtie back to the file based on the new max length
  final_text = ""
  loop = 0 

  while loop < len(file_list):
    for col in range(len(file_list[loop])):
      if column_index == None or col not in column_index:
        text = f"{file_list[loop][col].ljust(max_length_list[col] + 5)}"
        final_text += text

    final_text += "\n"
    loop +=1     

  print(final_text)


def pretty_table(filename, file_list):  
  # Get the max length of the string in each column
  max_length_list = []
  max_length = 0

  col = 0

  while col < len(file_list[0]):
    for row in file_list:
      if max_length < len(row[col]):
        max_length = len(row[col])
    
    max_length_list.append(max_length)
    max_length = 0
    col += 1
   
  # Reformat and wrtie back to the file based on the new max length
  with open(filename, "w") as af:
    final_text = ""
    loop = 0 

    while loop < len(file_list):
      for col in range(len(file_list[loop])):
        text = f"{file_list[loop][col].ljust(max_length_list[col] + 5)}"
        final_text += text
      

      final_text += "\n"
      loop +=1     
    af.write(final_text)



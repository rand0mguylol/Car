# Allows a list of column to not be display

# def pretty_table_display(file_list, column_list = None):
#   # file_list = format_file_list.format_file_list(filename)
  
#   # Get the max length of the string in each column
#   max_length_list = []
#   max_length = 0
#   for col in range(len(file_list[0])):
#     for row in range(len(file_list)):
#       if max_length < len(file_list[row][col]): 
#         max_length = len(file_list[row][col])
#     max_length_list.append(max_length)
#     max_length = 0
  
#   # Reformat and wrtie back to the file based on the new max length
#   final_text = ""
#   t = 0 
#   limit = 0
#   while t < len(file_list):
#     if column_list == None:
#       for col in range(len(file_list[0])):
#         for length in range(len(max_length_list)):
#             if col == length:
#               text = f"{file_list[t][col].ljust(max_length_list[length] + 5)}"
#               final_text += text
      
#       final_text += "\n"
#       t +=1     

#     else:
#       for col in range(len(file_list[0])):
#         for col_exception in column_list:
#           if col == col_exception:
#             file_list[t].pop(col_exception)

#       for col in range(len(max_length_list)):
#         for col_exception in column_list:
#           if col == col_exception:
#             max_length_list.pop(col_exception)    

#       for col in range(len(file_list[0])):
#         for length in range(len(max_length_list)):
#           if col != length:
#             text = f"{file_list[t][col].ljust(max_length_list[length] + 5)}"
#             final_text += text
      
#       final_text += "\n"
#       t +=1 
 

#   print(final_text)

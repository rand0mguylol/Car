# The use of this function is to print the columns in the file correctly
# Returns a list of list
# Each line is a list in the outer list
# Each column is an element in the inner list



def format_file_list(filename, list_option = None):

  file_list = []
  whitespace = "     "
  
  # if list_option == None:
  with open(filename, "r") as rf:
    for lines in rf:
      temp_list = []
      lines_list = lines.strip().split(whitespace)
      for element in lines_list:
        if element != "":
          element = element.strip()
          temp_list.append(element)

      if len(temp_list) > 0:
        file_list.append(temp_list)
  
  return file_list






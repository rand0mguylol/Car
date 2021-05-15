# This is a login system for ADMIN and REGISTERED CUSTOMER
# The use of this function is to ensure the account exists by checking each info with the data in the text file


from format_file_list import format_file_list

def login_validation(filename, id, email, password):
  id_exist = False
  admin_info_list = []

  file_list = format_file_list(filename)

  for row in file_list:
    if row[0] == id:
      id_exist = True
      admin_info_list = list(row)

    
  if id_exist == False:
      print("ID does not exist\n")
      return False

  if email == admin_info_list[1] and password == admin_info_list[2]:
      # print(header, end = "")
      # print(lines, end = "")
      return True
  else:
      print("The email or password entered is incorrect")
      return False



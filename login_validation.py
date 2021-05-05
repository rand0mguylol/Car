# This is a login system for ADMIN and REGISTERED CUSTOMER
# The use of this function is to ensure the account exists by checking each info with the data in the text file

# def login_validation(filename, id, email, password):
#   id_exist = False
#   with open (filename, "r") as rf:
#     # header = rf.readline()
#       for lines in rf:
#         l_list = []
#         lines_list = lines.split("     ")
#         for element in lines_list:
#           if element != "":
#             element = element.strip()
#             l_list.append(element)
#         if l_list[0] == id:
#           id_exist = True
#           info_list = list(l_list)
    
#       if id_exist == False:
#         print("ID does not exist")
#         return False

#       if email == info_list[1] and password == info_list[2]:
#         # print(header, end = "")
#         # print(lines, end = "")
#         return True
#       else:
#         print("The email or password entered is incorrect")
#         return False


# a = login_validation("admin.txt", "AD1", "", "")
# print(a)

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
      print("ID does not exist")
      return False

  if email == admin_info_list[1] and password == admin_info_list[2]:
      # print(header, end = "")
      # print(lines, end = "")
      return True
  else:
      print("The email or password entered is incorrect")
      return False


# a = login_validation("admin.txt", "AD1", "zxtey@gmail.com", "iam@dmin1")
# print(a)

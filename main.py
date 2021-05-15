from login_validation import login_validation
from pretty_table import pretty_table
from format_file_list import format_file_list
from pretty_table import pretty_table_display

def admin_main():
  admin_function_1 = [admin_login, exit]
  text = (f"{'Admin Menu'.center(45)}\n1. Login to access system\n2.Exit")

  function_validation(admin_function_1)


def function_validation(function_list, text = None):
  option = None

  while option == None:
    if text == None:
      pass
    else:
      print(text)
    option = input("Please choose an option by entering a number: ")
    print("")
    while not option.isdigit() or not 0 < int(option) <= len(function_list):
      option = None
      print("Please enter a valid option\n")
      break
  
  option = int(option)
  function_list[option - 1]()


def add_cars(file_name):
  user_list = []
  file_list = format_file_list(file_name)
  with open(file_name , "r") as af:
    total_lines = af.readlines()
    user_list.append(f"CA{len(total_lines)}")
    car_details_list = ["Maker: ", "Model: ", "Seats: ", "Class: ", "Plate Number: ", "Price(Hour): "]
    for details in car_details_list:
      user_list.append(input(f"{details}").strip())    

  user_list.append("TRUE")
    
  file_list.append(user_list)
  print(file_list)
  
  pretty_table(file_name, file_list)
    



def available_cars():
  isavailable_index = 8
  details_list = []

  file_list = format_file_list("car.txt")
  header = file_list[0]

  details_list.append(header)

  for row in file_list:
    if row[isavailable_index] == "TRUE":
      details_list.append(row)

  pretty_table_display(details_list, [isavailable_index])


       



def admin_login():
  id = input("Please enter ID: ").strip()
  email = input("Please enter email: ").strip()
  password = input("Please enter password: ").strip()

  is_login = login_validation("admin.txt", id, email, password)

  if is_login == True:
    admin_main_2()
  elif is_login == False:
    print("Enter 0 to retry. Enter 1 to exit")
    user_option = ""
    while not user_option.isdigit() or not 0 <= int(user_option) <= 1:
      user_option = input("Please choose an option: ")
      while not user_option.isdigit() or not 0 <= int(user_option) <= 1:
        print("Please enter a valid option\n")
        print("Enter 0 to retry. Enter 1 to exit")
        user_option = ""
        
  
    user_option = int(user_option)
    if user_option == 0:
      admin_login()
    else:
      admin_main()


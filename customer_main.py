from option_validation import option_validation
from main import available_cars
from fucntion_validation import function_validation
from format_file_list import format_file_list
from pretty_table import pretty_table
from login_validation import login_validation

def customer_main():
  customer_function = [available_cars, login_customer_account, register_customer_account, exit]
  text = (f"{'Customer Menu'.center(45)}\n1. View cars available for rent\n2. Login to account\n3. Register for an account\n4. Exit")
  

  function_validation(customer_function, text)


def register_customer_account():
  user_list = []
  file_list = format_file_list("customer.txt")
  with open("customer.txt" , "r") as af:
    total_lines = af.readlines()
    user_list.append(f"CU{len(total_lines)}")
    customer_details_list = ["Email: ", "Password: ", "Contact: ", "First Name: ", "Last Name: ", "Date of Birth (yyyy/mm/dd): ", "Address Line: ", "City: ", "State: ", "Postcode: "]
    for details in customer_details_list:
      user_list.append(input(f"{details}").strip())    

  user_list.append("TRUE")
  user_list.append("TRUE")
    
  file_list.append(user_list)
  print(file_list)
  
  pretty_table("customer.txt", file_list)
  
  exit_text = "Press 1 to exit"
  exit_option = option_validation(1, 1, exit_text)
  if int(exit_option) == 1:
    customer_main()

    
def login_customer_account():
  id = input("Please enter ID: ").strip()
  email = input("Please enter email: ").strip()
  password = input("Please enter password: ").strip()

  is_login = login_validation("customer.txt", id, email, password)

  if is_login == True:
    print("Login Successful")
  elif is_login == False:
    print("\nEnter 0 to retry. Enter 1 to exit")
    user_option = input("Please choose an option: ")
    print("")
    while not user_option.isdigit() or not 0 <= int(user_option) <= 1:
      print("\nPlease enter a valid option\n")
      print("Enter 0 to retry. Enter 1 to exit")
      user_option = input("Please choose an option: ")
      print("")
        
  
    user_option = int(user_option)
    if user_option == 0:
      login_customer_account()
    else:
      customer_main()

customer_main()
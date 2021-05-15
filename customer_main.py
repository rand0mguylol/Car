from get_id import get_id_info
from admin_main import rented_cars
from input_formatting import input_formatting
from option_validation import option_validation
from fucntion_validation import function_validation
from format_file_list import format_file_list
from pretty_table import pretty_table, pretty_table_display
from login_validation import login_validation
from admin_main import available_cars




def register_customer_account():
  user_list = []
  file_list = format_file_list("customer.txt")
  with open("customer.txt" , "r") as af:
    total_lines = af.readlines()
    user_list.append(f"CU{len(total_lines)}")
    customer_details_list = ["Email: ", "Password: ", "Contact: ", "First Name: ", "Last Name: ", "Date of Birth (yyyy/mm/dd): ", "Address Line: ", "City: ", "State: ", "Postcode: "]
    for details in customer_details_list:
      user_input = input(f"{details}") 
      if user_input == "":
        exit()
      else: 
        user_list.append(input_formatting(user_input))

  user_list.append("FALSE")
  user_list.append("TRUE")
    
  file_list.append(user_list)
  
  pretty_table("customer.txt", file_list)
  

    
def login_customer_account():
  id = input("Please enter ID: ").strip()
  email = input("Please enter email: ").strip()
  password = input("Please enter password: ").strip()

  is_login = login_validation("customer.txt", id, email, password)

  if is_login == True:
    print("Login Successful")
    customer_main_2(id)
  elif is_login == False:   
    text =  "Enter 0 to retry. Enter 1 to exit"
    user_option = option_validation(0, 1, text)

    if user_option == 0:
      login_customer_account()
    else:
      customer_main()


def personal_rental_history(id):
  
  # The first 3 variable defined here is used to get the correct info from the rentedcar.txt
  customer_id_index = 3
  car_id_index = 2
  status = 1

  # car_id_list is used to store the id of the cars rented by the user. 
  cars_id_list = []

  # These variables are used to retrive specific info from the rentedcar.txt that is associated with the id provided in the argument. 
  rented_details = []
  needed_info_index = [1, 4, 5, 6, 7, 8]

  
  rented_cars_list = format_file_list("rentedcar.txt")

  headers = rented_cars_list[0]
  temp_list = [(headers[x]) for x in needed_info_index]
  rented_details.append(temp_list)

  for row in rented_cars_list:
    if row[status] == "INUSE" or row[status] == "RETURNED":
      if row[customer_id_index] ==  id:
        cars_id_list.append(row[car_id_index])
        temp_list = [row[x] for x in needed_info_index]
        rented_details.append(temp_list)


  personal_rental_list = get_id_info("car.txt", cars_id_list)

  # There will be 2 list of list here: personal_rental_list and rented_details
  # We loop through personal_rental_list.
  # For each list in personal_rental_list, we append each element in the list in rented_details.
  # Since both list of list contain the same list, we can just use range(len)
  for i in range(len(personal_rental_list)):
    for x in rented_details[i]:
      personal_rental_list[i].append(x)
   

  pretty_table_display(personal_rental_list, [8])
  





def customer_main():

  while True:
    customer_function = [available_cars, login_customer_account, register_customer_account, exit]
    text = (f"{'Customer Menu'.center(45)}\n\n1. View cars available for rent\n2. Login to account\n3. Register for an account\n4. Exit")
      

    function_validation(customer_function, text)









# customer_main()

# def customer_main_2(id):
#   customer_function_2 = [personal_rental_history]
#   text = "TEST"
#   function_validation(customer_function_2, text, id)



# customer_main_2()





# def modify_customer_details(id):
#   customer_file_list = format_file_list("customer.txt")
  
#   count = 0

#   for row in customer_file_list:
#     if row[0] == id:
#       personal_details_index = count
#       break

#     count += 1

#   personal_details_list = customer_file_list.pop(personal_details_index)
#   headers = customer_file_list[0]

#   for i in range(len(headers)):
#     if i == 2:
#       print(headers[i].ljust(15), ": ", "*" * len(personal_details_list[i]))
#     else:
#        print(headers[i].ljust(15), ": ", personal_details_list[i])
    
#   print(headers[2:11])
  
  

# def modify_password(old_password):
#   user_input = input("Please enter your old password: ")
#   while True:
#     if user_input == old_password:
#       new_password = input("Please enter your new password: ")
#       print(new_password)
#       break
#     else:
#       print("Password does not match")
#       text = ("Enter 0 to try again, enter 1 to exit")
#       answer = option_validation(0, 1, text)
#       if answer == 0:
#         user_input = input("Please enter your old password: ")      
#       else: 
#         return
      




def do_payment(id):
  
  payment_status_index = 7
  car_id = 2
  customer_id_index = 3
  booking_exist = False
  status_index = 1
  car_id_list = []
  needed_info_index = [4, 5, 6, 7, 8]
  needed_details = []

  is_paid = False

  rented_file_list = format_file_list("rentedcar.txt")
  headers = rented_file_list[0]

  needed_details.append([headers[x] for x in needed_info_index])
  
  for row in rented_file_list:
    if row[customer_id_index] == id and row[status_index] == "BOOKED" and row[payment_status_index] == "PENDING" :
      needed_details.append(row[x] for x in needed_info_index)
      booking_exist = True
      car_id_list.append(row[car_id])
      break

  if booking_exist == False:
    print("No pending payment")
    exit()

  car_list = get_id_info("car.txt", car_id_list)

  for i in range(len(car_list)):
    for x in needed_details[i]:
      car_list[i].append(x)

  pretty_table_display(car_list, [8])
  
  while True: 
    print("Enter YES to pay. Enter NO to exit")
    user_option = input("Option: ")

    if user_option == "YES":
      print("Payment Successful")
      is_paid = True
      break
    elif user_option == "NO":
      exit()
    else:
      print("Please enter a valid option.")

  
  if is_paid == True:
    for row in rented_file_list:
      if row[customer_id_index] == id and row[status_index] == "BOOKED":
        row.remove("PENDING")
        row.insert(payment_status_index, "PAID")
  
  pretty_table("rentedcar.txt", rented_file_list)



do_payment("CU1")



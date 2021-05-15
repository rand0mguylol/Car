from datetime import time
from format_file_list import format_file_list
from pretty_table import pretty_table_display, pretty_table
from fucntion_validation import function_validation
from option_validation import option_validation
from login_validation import login_validation
from get_id import get_id_info


def admin_main():
  admin_function_1 = [admin_login, exit]
  text = (f"{'Admin Menu'.center(45)}\n1. Login to access system\n2. Exit")

  function_validation(admin_function_1, text)


def add_cars():
  user_list = []
  file_list = format_file_list("car.txt")
  with open("car.txt" , "r") as af:
    total_lines = af.readlines()
    user_list.append(f"CA{len(total_lines)}")
    car_details_list = ["Maker: ", "Model: ", "Seats: ", "Class: ", "Plate Number: ", "Price(Hour): "]
    for details in car_details_list:
      user_list.append(input(f"{details}").strip())    

  user_list.append("TRUE")
    
  file_list.append(user_list)
  print(file_list)
  
  pretty_table("car.txt", file_list)
    



def available_cars():
  # isavailable_index is used to locate the info we need from rentedcar.txt.
  isavailable_index = 8

  # The details_list is used to store the available cars
  details_list = []

  file_list = format_file_list("car.txt")
  header = file_list[0]

  details_list.append(header)

 # Each row is a list
 # row[isavailable_index] returns a string
  for row in file_list:
    if row[isavailable_index] == "TRUE":
      details_list.append(row)


  pretty_table_display(details_list, [isavailable_index])

  exit_text = "Press 1 to exit"
  exit_option = option_validation(1, 1, exit_text)
  if exit_option == 1:
    return

  



def filter_payment():

  # The first 3 variable is used to locate the info from rentedcar.txt  
  payment_period_column = 8
  car_id_index = 2
  customer_id_index = 3
  
   # The id list is used to store the car id and customer id associated with the specific duration we need
  car_id_list = []
  customer_id_list = []

  time_filter = ""

  text = ("Please choose a filter option\n1. Days\n2. Hours\n3. EXIT TO ADMIN MENU")
  option = option_validation(1, 3, text)
  

  # Here we assign time_filter to be either DAYS or HOURS based on the option
  if option == 1:
    time_filter = "DAYS"
  elif option == 2:
    time_filter = "HOURS"


#  Here we obtain the time duration
  while True:
    time_duration = input(f"Please choose a duration ({time_filter.title()}): ")
    try:
      float(time_duration)
      break
    except:
        print("\nPlease enter a valid option\n")
        continue


  rented_car_file_list = format_file_list("rentedcar.txt")
  header = rented_car_file_list[0]

# The details_list is used to store the line with the specific time duration we're looking for in the rentedcar.txt
  details_list = []
  details_list.append(header)

# Each row is a list, so row[payment_period_column] will return a string
# We check to see if time_filter, either DAYS or HOURS is in the row[payment_period_column]
# If yes, we will split row[payment_period_column]
  for row in rented_car_file_list:
    if time_filter in row[payment_period_column]:
      time_number = row[payment_period_column].split(f" {time_filter}") # Getting rid of the word (DAYS/HOURS) and getting the number only  
      if time_duration in time_number:  #length of time_number(list) will be 1 or 0. If the time_duration is in the list, we will append the row.
        details_list.append(row) 
        # Since we're just displaying the info, this is to ensure the id will not be repeated in the list. All the necessary info is in details_list
        # These 2 list below are just additional info.
        car_id_list.append(row[car_id_index]) if row[car_id_index] not in car_id_list else False
        customer_id_list.append(row[customer_id_index]) if row[customer_id_index] not in customer_id_list else False
    
  car_list = get_id_info("car.txt", car_id_list)
  customer_list = get_id_info("customer.txt", customer_id_list)
  
  pretty_table_display(details_list)
  pretty_table_display(car_list, [8])
  pretty_table_display(customer_list, [2]) # 2 in the parameter to prevent displaying customer password



def admin_login():
  id = input("Please enter ID: ").strip()
  email = input("Please enter email: ").strip()
  password = input("Please enter password: ").strip()

  # login_validation will return a boolean 
  is_login = login_validation("admin.txt", id, email, password)

  # If true, the login info is found in the file
  if is_login == True:
    print("")
    print("LOGIN SUCCESSFUL\n".center(45))
    admin_main_2()
  # If false, we will prompt the user to retry or exit if they want
  elif is_login == False:
    text = "Enter 0 to retry. Enter 1 to exit"
    user_option = option_validation(0, 1, text)
        
    if user_option == 0:
      admin_login()
    else:
      admin_main()



def rented_cars():
  # The first 3 variable is used to obtain the info from rentedcar.txt  
  status_index = 1
  car_id_index = 2
  customer_id_index = 3

 # The id list is used to store the car id and customer id associated with the booked cars we need
  car_id_list = []
  customer_id_list = []
  rented_car_list = []

  rented_car_file_list = format_file_list("rentedcar.txt")
  header = rented_car_file_list[0]

  rented_car_list.append(header)

  for row in rented_car_file_list:
    if row[status_index] == "INUSE":
      rented_car_list.append(row)
      # Since we're just displaying the infos of the car, this is to ensure the id will not be repeated in the list. All the necessary info is in rented_car_list
      # Therse 2 list below are just additional info.
      car_id_list.append(row[car_id_index]) if row[car_id_index] not in car_id_list else False
      customer_id_list.append(row[customer_id_index]) if row[customer_id_index] not in customer_id_list else False

  # car_file_list = format_file_list("car.txt")
  # car_list.append(car_file_list[0]) # Append header
  # for row in car_file_list:
  #   for id in car_id_list:
  #     if row[0] == id:
  #       car_list.append(row)

  car_list = get_id_info("car.txt", car_id_list)
  customer_list = get_id_info("customer.txt", customer_id_list)


  pretty_table_display(rented_car_list)
  pretty_table_display(car_list, [8])
  pretty_table_display(customer_list, [2])
  

def booked_cars():
  # The first 3 variable is used to obtain the info from rentedcar.txt
  status_index = 1
  car_id_index = 2
  customer_id_index = 3

 # The id list is used to store the car id and customer id associated with the booked cars we need
  car_id_list = []
  customer_id_list = []
  
  rented_car_list = []


  rented_car_file_list = format_file_list("rentedcar.txt")
  header = rented_car_file_list[0]

  rented_car_list.append(header)

 # We check the word in the statuds_index to ensure it is "BOOKED"
  for row in rented_car_file_list:
    if row[status_index] == "BOOKED":
      rented_car_list.append(row)
      # Since we're just displaying the infos of the car, this is to ensure the id will not be repeated in the list. All the necessary info is in rented_car_list
      # Therse 2 list below are just additional info.
      car_id_list.append(row[car_id_index]) if row[car_id_index] not in car_id_list else False
      customer_id_list.append(row[customer_id_index]) if row[customer_id_index] not in customer_id_list else False

  car_list = get_id_info("car.txt", car_id_list)
  customer_list = get_id_info("customer.txt", customer_id_list)


  pretty_table_display(rented_car_list)
  pretty_table_display(car_list, [8])
  pretty_table_display(customer_list, [2])



def admin_main_2():
  admin_function_2 = [add_cars, rented_cars, available_cars, booked_cars, filter_payment, admin_main]
  text = (f"{'Admin Menu'.center(45)}\n1. Add cars to be rented out\n2. Display rented cars\n3. Display available cars\n4. Display booked cars\n5. Filter customer payment duration\n6. Exit")

  function_validation(admin_function_2, text)

  text = "Press 1 to exit"
  exit_option = option_validation(1, 1, text)
  if exit_option == 1:
    admin_main_2()


  
  



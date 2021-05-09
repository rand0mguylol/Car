from format_file_list import format_file_list
from pretty_table import pretty_table_display
from fucntion_validation import function_validation
from option_validation import option_validation

def admin_main():
  admin_function_1 = [admin_login, exit]
  text = (f"{'Admin Menu'.center(45)}\n1. Login to access system\n2.Exit")

  function_validation(admin_function_1)



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
  isavailable_index = 7
  details_list = []

  file_list = format_file_list("car.txt")
  header = file_list[0]

  details_list.append(header)


  for row in file_list:
    if row[isavailable_index] == "TRUE":
      details_list.append(row)

  pretty_table_display(details_list, 1)






def filter_payment(filename):
  payment_period_column = 8
  car_id_index = 2
  customer_id_index = 3
  car_id_list = []
  customer_id_list = []
  car_list = []
  customer_list = []
  time_filter = ""

  text = ("Please choose a filter option\n1. Days\n2. Hours")
  option = option_validation(1, 2, text)
  
  if option == 1:
    time_filter = "DAYS"
  elif option == 2:
    time_filter == "HOURS"


  time_duration = input(f"Please choose a duration ({time_filter.title()}): ")
  while not time_duration.isdigit():
    print("\nPlease enter a valid option\n")
    time_duration = input(f"Please choose a duration ({time_filter.title()}): ")
  

  rented_car_file_list = format_file_list(filename)
  header = rented_car_file_list[0]

  details_list = []
  details_list.append(header)

  for row in rented_car_file_list:
    if time_filter in row[payment_period_column]:
      time_number = row[payment_period_column].split(f" {time_filter}") # time_number is a list
      if time_duration in time_number: 
        details_list.append(row)
        car_id_list.append(row[car_id_index])
        customer_id_list.append(row[customer_id_index])
  
  car_file_list = format_file_list("car.txt")
  car_list.append(car_file_list[0]) # Append header
  for row in car_file_list:
    for id in car_id_list:
      if row[0] == id:
        car_list.append(row)

  customer_file_list = format_file_list("customer.txt")
  customer_list.append(customer_file_list[0]) # Append header
  for row in customer_file_list:
    for id in customer_id_list:
      if row[0] == id:
        customer_list.append(row)
  
  pretty_table_display(details_list)
  pretty_table_display(car_list, 7)
  pretty_table_display(customer_list, 2)



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


filter_payment("rentedcar.txt")
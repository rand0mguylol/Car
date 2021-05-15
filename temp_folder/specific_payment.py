from pretty_table import pretty_table_display
from format_file_list import format_file_list
from option_validation import option_validation
from get_id import get_id_info

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
  option = option_validation(text, 1, 2)
  
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
        car_id_list.append(row[car_id_index]) if row[car_id_index] not in car_id_list else False
        customer_id_list.append(row[customer_id_index]) if row[customer_id_index] not in customer_id_list else False
 

  car_list = get_id_info("car.txt", car_id_list)
  customer_list = get_id_info("customer.txt", customer_id_list)
  
  pretty_table_display(details_list)
  pretty_table_display(car_list, [7])
  pretty_table_display(customer_list, [2])


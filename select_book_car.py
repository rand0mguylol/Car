from temp_folder.paymentperiod import payment_period
from admin_main import rented_cars
import datetime
from date_validation import date_validation
from pretty_table import pretty_table, pretty_table_display
from format_file_list import format_file_list

def select_book_car(id):
  
  status = 1
  customer_id_index = 3
  is_available_index = 8
  is_available_cars = []
  car_exist = False

  # We need to do a check first to ensure the customer has not booked a car or
  # is not currently renting a car.
  
  rented_list = format_file_list("rentedcar.txt")

  for row in rented_list:
    if row[customer_id_index] == id:
      if row[status] == "BOOKED":
        print("You already have a booking")
        exit()
      if row[status] == "INUSE":
        print("You already have a rented car")
        exit()      

  car_file_list = format_file_list("car.txt")
  is_available_cars.append(car_file_list[0])

  for row in car_file_list:
    if row[is_available_index] == "TRUE":
      is_available_cars.append(row)

  while car_exist == False:
    pretty_table_display(is_available_cars, [is_available_index])

    car_id = input("Enter the ID of the car you would like to book. Leave field blank to ewit: ").strip()

    for row in is_available_cars:
      if row[0] == car_id:
        car_exist = True
        break
      elif car_id == "":
        return
      
    if car_exist == False:
      print("Car does not exist\n")
    
  booking_date = datetime.datetime.now().replace(microsecond=0)
  pickup_text = "Please select a pickup date (yyyy/mm/dd) (hh:mm:ss) (24 hours format) (Leave blank to exit): "
  dropoff_text = "Please select a dropoff date (yyyy/mm/dd) (hh:mm:ss) (24 hours format) (Leave blank to exit): "
  pickup_date = date_validation(pickup_text, display_time=True)

  if pickup_date == None:
    exit()

  dropoff_date = date_validation(dropoff_text, display_time=True)

  if dropoff_date == None:
    exit()

  rented_list.extend([(f"RC{len(rented_list)}", "BOOKED", car_id, id, str(booking_date), str(pickup_date), str(dropoff_date), "PENDING", payment_period(pickup_date, dropoff_date))])

  for row in car_file_list:
    if row[0] == car_id:
      row.remove("TRUE")
      row.append("FALSE")
  
  pretty_table("car2.txt", car_file_list)
  pretty_table("rentedcar.txt", rented_list)





select_book_car("CU1")
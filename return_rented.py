from format_file_list import format_file_list
from pretty_table import pretty_table, pretty_table_display

def return_rented():
  
  car_exist = False
  status_index = 1
  rented_file_list = format_file_list("rentedcar.txt")
  rented_cars = []

  rented_cars.append(rented_file_list[0])

  for row in rented_file_list:
    rented_cars.append(row) if row[status_index] == "INUSE" else False
  
  pretty_table_display(rented_cars)

  while car_exist == False:
    return_car_id = input("Enter the ID of the rented car you would like to return. Leave field blank to ewit: ").strip()
    for row in rented_cars:
      if row[0] == return_car_id:
        car_exist = True
        break
      elif return_car_id == "":
        exit()
      

    if car_exist == False:
      print("Car does not exist\n")
    

    for row in rented_file_list:
      if row[0] == return_car_id:
        row.pop(status_index)
        row.insert(status_index, "RETURNED")
    
    pretty_table("rentedcar.txt", rented_file_list)
   

  

return_rented()
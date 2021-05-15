from format_file_list import format_file_list
from pretty_table import pretty_table_display, pretty_table
from option_validation import option_validation

def modify_car_details():

  count = 0
  car_exist = False
  modify_text = ["Plate Number", "Price\Hour", "Price\Day"]
  modify_index = [5, 6, 7]

  car_list = format_file_list("car.txt")
  pretty_table_display(car_list)
 
  while car_exist == False:
    car_id = input("Enter the ID of the car you would like to modify. Leave field blank to ewit: ").strip()
    for row in car_list:
      if row[0] == car_id:
        target_index = count
        car_exist = True
        break
      elif car_id == "":
        exit()
      
      count += 1

    if car_exist == False:
      print("Car does not exist\n")


  header = car_list[0]
  target_list = car_list.pop(target_index)
  
  print("")
  for i in range(len(header)):
    print(header[i].ljust(15), ":   ", target_list[i])
  print("")

  text = "Please choose an option to modify.\n1.Plate Number\n2. Price\Hour\n3. Price\Day"

  modify_option = option_validation (1, 3, text)

  if modify_option == None:
    exit()


  new_modification = input(f"Please enter new {modify_text[modify_option - 1]}: ")
  target_list.pop(modify_index[modify_option - 1])
  target_list.insert(modify_index[modify_option - 1], new_modification)

  car_list.insert(target_index, target_list)
  
  pretty_table("car.txt", car_list)


modify_car_details() 
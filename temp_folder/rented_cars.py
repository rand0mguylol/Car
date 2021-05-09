from ....PWP2.parent.public_functions.format_file_list import format_file_list


# Returns details on cars that have been rented out, details of the respective cars, the customer details who rented car.

# NEW VERSION
def car_status(filename, status, displaycar = False, displaycustomer = False):
  status_index = 1
  car_id_index = 2
  customer_id_index = 3
  car_id_list = []
  customer_id_list = []
  rented_car_list = []
  car_list = []
  customer_list = []

  rented_car_file_list = format_file_list(filename)
  header = rented_car_file_list[0]

  rented_car_list.append(header)

  if status == "RENTED":   
    for row in rented_car_file_list:
      if row[status_index] == "INUSE":
        rented_car_list.append(row)
        car_id_list.append(row[car_id_index])
        customer_id_list.append(row[customer_id_index])

  if status == "BOOKED":
    for row in rented_car_file_list:
      if row[status_index] == "BOOKED":
        rented_car_list.append(row)
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
     

  pretty_table_display(rented_car_list)
  if displaycar == True:
    pretty_table_display(car_list, 7)
  if displaycustomer == True:
    pretty_table_display(customer_list, 2)
  
  print(car_id_list)


car_status("rentedcar.txt", "BOOKED", True, True)


# def seraching(filename, column, specific_info, displaycar = False, displaycustomer = False):
#   # column = "CARID"
#   car_id_col = "CARID"
#   customer_id_col = "CUSTOMERID"
#   column_index = 0
#   car_id_index = 0
#   customer_id_index = 0
#   car_id_list = []
#   customer_id_list = []
#   rented_car_list = []
#   car_list = []
#   customer_list = []

#   file_list = format_file_list(filename)
#   header = file_list[0]
#   for index in range(len(header)):
#     if header[index] == column:
#       column_index = index
#     if header[index] == car_id_col:
#       car_id_index = index
#     if header[index] == customer_id_col:
#       customer_id_index = index

#   rented_car_list.append(header)

#   for row in range(len(file_list)):    #Loop through outer list  # Range is number of list in outer list
#       if file_list[row][column_index] == specific_info:
#         rented_car_list.append(file_list[row])
#         car_id_list.append(file_list[row][car_id_index])
#         customer_id_list.append(file_list[row][customer_id_index])
  
#   car_file_list = format_file_list("car.txt")
#   car_list.append(car_file_list[0])
#   for row in car_file_list:
#     for id in car_id_list:
#       if row[0] == id:
#         car_list.append(row)

#   customer_file_list = format_file_list("customer.txt")
#   customer_list.append(customer_file_list[0])
#   for row in customer_file_list:
#     for id in customer_id_list:
#       if row[0] == id:
#         customer_list.append(row)
     

#   pretty_table_display(rented_car_list)
#   if displaycar == True:
#     pretty_table_display(car_list, 7)
#   if displaycustomer == True:
#     pretty_table_display(customer_list, 2)


# seraching("rentedcar.txt", "CARID", "CA1", True, True)
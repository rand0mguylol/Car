# The use of this function is to ensure the correct function will be ran according to the user option
# It also ensures the user selects only the options displayed on the screen and not any invalid data


def function_validation(function_list, text = None, customer_id = None):

  if text != None:
    print(text)

  option = input("Please choose an option by entering a number: ")
  print("")

  while not option.isdigit() or not 0 < int(option) <= len(function_list):
    print("Please enter a valid option\n")
    
    if text != None:
      print(text)

    option = input("Please choose an option by entering a number: ")
    print("")

  
  option = int(option)
  
  if customer_id == None:
    function_list[option - 1]()
  else:
    function_list[option - 1](customer_id)








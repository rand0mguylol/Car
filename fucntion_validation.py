# The use of this function is to ensure the correct function will be ran according to the user option
# It also ensures the user selects only the options displayed on the screen and not any invalid data


def function_validation(function_list, text = None):
  option = None

  while option == None:
    if text == None:
      pass
    else:
      print(text)
    option = input("Please choose an option by entering a number: ")
    print("")
    while not option.isdigit() or not 0 < int(option) <= len(function_list):
      option = None
      print("Please enter a valid option\n")

  
  option = int(option)
  function_list[option - 1]()

